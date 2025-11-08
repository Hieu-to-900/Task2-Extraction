"""
MCQ Batch Processor and Evaluation System
Handles CSV processing, batch inference, and evaluation against ground truth
"""

import pandas as pd
import time
import re
from typing import List, Dict, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from rag_system import VietnameseMCQRAG, RAGConfig, Logger


class DebugSession:
    """Handle interactive debugging session for multiple questions"""
    
    def __init__(self, rag_system: VietnameseMCQRAG):
        self.rag_system = rag_system
        self.logger = rag_system.logger
        self.config = rag_system.config
        self.questions_df = None
        self.ground_truth = None
        self.total_questions = 0
        
    def initialize(self):
        """Initialize debug session by loading data once"""
        try:
            # Load questions and ground truth once
            self.questions_df = self._load_questions(self.config.QUESTIONS_PATH)
            self.ground_truth = self._load_ground_truth(self.config.TRUE_RESULTS_PATH)
            self.total_questions = len(self.questions_df)
            
            print(f"✅ Debug session initialized. Available questions: 1-{self.total_questions}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to initialize debug session: {str(e)}")
            return False
    
    def _load_questions(self, file_path: str):
        """Load questions from CSV file"""
        import pandas as pd
        
        df = pd.read_csv(file_path, encoding='utf-8')
        expected_columns = ['Question', 'A', 'B', 'C', 'D']
        if not all(col in df.columns for col in expected_columns):
            raise ValueError(f"CSV must have columns: {expected_columns}")
        return df
    
    def _load_ground_truth(self, file_path: str):
        """Load ground truth results"""
        results = []
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for line in lines[1:]:  # Skip header
            line = line.strip()
            if not line:
                continue
                
            if ',' in line:
                parts = line.split(',', 1)
                num_correct = int(parts[0])
                answers_str = parts[1].strip('"')
                
                if answers_str:
                    answers = [a.strip() for a in answers_str.split(',')]
                else:
                    answers = []
                
                results.append((num_correct, answers))
        
        return results
    
    def is_valid_question_id(self, question_id):
        """Check if question ID is valid"""
        return 1 <= question_id <= self.total_questions
    
    def debug_question(self, question_id: int):
        """Debug a specific question"""
        if not self.is_valid_question_id(question_id):
            print(f"❌ Invalid question ID: {question_id}. Must be between 1 and {self.total_questions}")
            return False
        
        try:
            # Get question data (convert to 0-based index)
            question_idx = question_id - 1
            row = self.questions_df.iloc[question_idx]
            
            # Extract question and options
            question = row['Question']
            options = {
                'A': row['A'],
                'B': row['B'], 
                'C': row['C'],
                'D': row['D']
            }
            
            # Get ground truth for this question
            if question_idx < len(self.ground_truth):
                actual_num, actual_answers = self.ground_truth[question_idx]
            else:
                actual_answers = []
            
            # Clear screen separator
            print("\n" + "🔍" + "="*79)
            print("1. INPUT ANALYSIS")
            print("="*80)
            print(f"Question ID: {question_id}")
            print(f"Question: {question}")
            print("Options:")
            for key, value in options.items():
                print(f"  {key}: {value}")
            
            # Get debug info from RAG system
            debug_info = self.rag_system.answer_mcq_debug(question, options)
            
            print("\n" + "="*80)
            print("2. QUERY REFORMULATION")
            print("="*80)
            original_query = debug_info.get('original_query', question)
            reformulated_query = debug_info.get('reformulated_query', question)
            print(f"Original Query: {original_query}")
            print(f"Reformulated Query: {reformulated_query}")
            
            print("\n" + "="*80)
            print("3. RETRIEVED CONTEXT\n")
            #print("="*80)
            print(f"Top {len(debug_info['retrieved_chunks'])} chunks retrieved:")
            for i, (chunk, score) in enumerate(debug_info['retrieved_chunks'], 1):
                print(f"[Score: {score:.3f}] | [Chunk {i}]: {chunk}")
                print()
            
            print("\n" + "="*80)
            print("4. RAW MODEL RESPONSE\n")
            #print("="*80)
            print(debug_info['raw_response'])
            
            print("\n" + "="*80)
            print("5. RESULT ANALYSIS")
            # print("="*80)
            predicted_answers = debug_info['parsed_answers']
            
            print(f"\nExpected Answer: {actual_answers}")
            print(f"Predicted Answer: {predicted_answers}")
            
            # Calculate detailed scoring
            if actual_answers:
                predicted_set = set(predicted_answers)
                actual_set = set(actual_answers)
                
                k = len(actual_set)  # number of correct answers
                c = len(predicted_set & actual_set)  # correct answers selected
                w = len(predicted_set - actual_set)  # wrong answers selected
                e = (k - c) + w  # total errors
                
                # Calculate score
                if e == 0:
                    score = 1.0
                    status = "✅ CORRECT"
                elif e == 1:
                    score = 0.5
                    status = "⚠️ PARTIAL"
                else:
                    score = 0.0
                    status = "❌ WRONG"
                
                print(f"Match Status: {status}")
                print(f"Score: {score}")
                       
            return True
            
        except Exception as e:
            print(f"❌ Debug failed for question {question_id}: {str(e)}")
            return False


class MCQProcessor:
    """Process MCQ questions in batches and evaluate results"""
    
    def __init__(self, rag_system: VietnameseMCQRAG):
        self.rag_system = rag_system
        self.logger = rag_system.logger
        self.config = rag_system.config
        
    def load_questions(self, file_path: str, limit: int = None, 
                     random_sampling: bool = False, range_spec: str = None) -> pd.DataFrame:
        """Load questions from CSV file with sampling options"""
        self.logger.log_info(f"Loading questions from: {file_path}")
        
        try:
            # Read CSV, skip header row
            df = pd.read_csv(file_path, encoding='utf-8')
            
            # Ensure we have the right columns
            expected_columns = ['Question', 'A', 'B', 'C', 'D']
            if not all(col in df.columns for col in expected_columns):
                raise ValueError(f"CSV must have columns: {expected_columns}")
            
            total_questions = len(df)
            self.logger.log_info(f"Total questions available: {total_questions}")
            
            # Apply range filter if specified
            if range_spec:
                start, end = map(int, range_spec.split('-'))
                df = df.iloc[start-1:end]  # Convert to 0-based indexing
                self.logger.log_info(f"Using range {start}-{end}: {len(df)} questions")
            
            # Apply limit and sampling
            if limit and limit < len(df):
                if random_sampling:
                    import random
                    df = df.sample(n=limit, random_state=42)
                    self.logger.log_info(f"Random sampling: {limit} questions")
                else:
                    df = df.head(limit)
                    self.logger.log_info(f"Sequential sampling: first {limit} questions")
            
            self.logger.log_info(f"Final dataset: {len(df)} questions")
            return df
            
        except Exception as e:
            self.logger.log_error("Failed to load questions", e)
            raise
    
    def load_ground_truth(self, file_path: str) -> List[Tuple[int, List[str]]]:
        """Load ground truth results"""
        self.logger.log_info(f"Loading ground truth from: {file_path}")
        
        try:
            results = []
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # Skip header line
            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue
                    
                # Parse format: num_correct,answers
                if ',' in line:
                    parts = line.split(',', 1)
                    num_correct = int(parts[0])
                    answers_str = parts[1].strip('"')
                    
                    # Parse answers
                    if answers_str:
                        answers = [a.strip() for a in answers_str.split(',')]
                    else:
                        answers = []
                    
                    results.append((num_correct, answers))
            
            self.logger.log_info(f"Loaded {len(results)} ground truth entries")
            return results
            
        except Exception as e:
            self.logger.log_error("Failed to load ground truth", e)
            raise
    
    def process_single_question(self, question_data: Tuple[int, pd.Series]) -> Tuple[int, List[str], float]:
        """Process a single question and return results with timing"""
        idx, row = question_data
        
        start_time = time.time()
        
        try:
            # Extract question and options
            question = row['Question']
            options = {
                'A': row['A'],
                'B': row['B'], 
                'C': row['C'],
                'D': row['D']
            }
            
            # Get answer from RAG system
            predicted_answers = self.rag_system.answer_mcq(question, options)
            
            processing_time = time.time() - start_time
            
            return idx, predicted_answers, processing_time
            
        except Exception as e:
            self.logger.log_error(f"Error processing question {idx}: {str(e)}")
            return idx, [], time.time() - start_time
    
    def batch_process_questions(self, questions_df: pd.DataFrame, 
                              max_workers: int = 4) -> List[Tuple[int, List[str], float]]:
        """Process questions in parallel batches with GPU optimization"""
        self.logger.log_info(f"Processing {len(questions_df)} questions with {max_workers} workers")
        
        # Check GPU availability and adjust strategy
        import torch
        use_gpu = torch.cuda.is_available()
        if use_gpu:
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
            self.logger.log_info(f"GPU optimization enabled: {gpu_name} ({gpu_memory:.1f}GB)")
            
            # For RTX 3090, we can use larger batch sizes
            if "3090" in gpu_name or gpu_memory > 20:
                max_workers = 1  # Sequential processing but with larger internal batches
                self.logger.log_info("RTX 3090 detected - using optimized sequential processing")
        
        results = []
        
        # Process questions (sequential for GPU optimization)
        self.logger.log_info("Processing questions sequentially for GPU optimization")
        
        start_time = time.time()
        for idx, row in questions_df.iterrows():
            result = self.process_single_question((idx, row))
            results.append(result)
            
            # Progress logging with ETA
            completed = len(results)
            total = len(questions_df)
            progress_pct = (completed / total) * 100
            
            if completed % max(1, total // 20) == 0:  # Log every 5%
                elapsed_time = time.time() - start_time
                avg_time_per_question = elapsed_time / completed
                remaining_questions = total - completed
                eta_seconds = remaining_questions * avg_time_per_question
                eta_minutes = eta_seconds / 60
                
                self.logger.log_info(
                    f"Progress: {completed}/{total} ({progress_pct:.1f}%) | "
                    f"Speed: {avg_time_per_question:.2f}s/question | "
                    f"ETA: {eta_minutes:.1f} minutes"
                )
                
                # Log GPU memory usage if available
                if use_gpu:
                    memory_allocated = torch.cuda.memory_allocated() / 1024**3
                    memory_reserved = torch.cuda.memory_reserved() / 1024**3
                    gpu_utilization = f"GPU Memory: {memory_allocated:.2f}GB allocated, {memory_reserved:.2f}GB reserved"
                    self.logger.log_info(gpu_utilization)
        
        # Sort results by question index
        results.sort(key=lambda x: x[0])
        
        self.logger.log_info("Batch processing completed")
        return results
    
    def calculate_score(self, predicted: List[str], actual: List[str]) -> float:
        """
        Calculate score based on new error-based criteria:
        N = 4 (total choices), k = number of correct answers, 
        c = number of correct answers selected by AI,
        w = number of wrong answers selected by AI,
        e = errors = (k - c) + w
        
        Score: Pmax=1.0 if e=0, 0.5*Pmax if e=1, 0 if e>=2
        """
        
        predicted_set = set(predicted)
        actual_set = set(actual)
        
        # Calculate parameters
        k = len(actual_set)  # number of correct answers (ground truth)
        c = len(predicted_set & actual_set)  # number of correct answers selected by AI
        w = len(predicted_set - actual_set)  # number of wrong answers selected by AI
        
        # Calculate errors
        e = (k - c) + w
        
        # Apply scoring rules
        if e == 0:
            return 1.0  # Perfect - no errors
        elif e == 1:
            return 0.5  # One error
        else:
            return 0.0  # Two or more errors
    
    
    def evaluate_results(self, predictions: List[Tuple[int, List[str], float]], 
                        ground_truth: List[Tuple[int, List[str]]]) -> Dict:
        """Evaluate predictions against ground truth"""
        
        self.logger.log_info("Evaluating results against ground truth")
        
        if len(predictions) != len(ground_truth):
            self.logger.log_error(f"Mismatch: {len(predictions)} predictions vs {len(ground_truth)} ground truth")
        
        scores = []
        detailed_results = []
        
        min_length = min(len(predictions), len(ground_truth))
        
        for i in range(min_length):
            pred_idx, predicted, proc_time = predictions[i]
            actual_num, actual_answers = ground_truth[i]
            
            # Calculate score
            score = self.calculate_score(predicted, actual_answers)
            scores.append(score)
            
            # Log individual result
            self.logger.log_question_result(
                pred_idx + 1, 
                ','.join(predicted) if predicted else 'None',
                ','.join(actual_answers) if actual_answers else 'None',
                score,
                proc_time
            )
            
            detailed_results.append({
                'question_idx': pred_idx + 1,
                'predicted': predicted,
                'actual': actual_answers,
                'score': score,
                'processing_time': proc_time
            })
        
        # Calculate final score
        total_score = sum(scores)
        final_score = (total_score / len(scores)) * 100 if scores else 0
        
        evaluation_summary = {
            'final_score': final_score,
            'total_questions': len(scores),
            'perfect_answers': sum(1 for s in scores if s == 1.0),
            'partial_answers': sum(1 for s in scores if s == 0.5),
            'wrong_answers': sum(1 for s in scores if s == 0.0),
            'average_processing_time': sum(r['processing_time'] for r in detailed_results) / len(detailed_results) if detailed_results else 0,
            'detailed_results': detailed_results
        }
        
        self.logger.log_info(f"Evaluation completed. Final score: {final_score:.2f}%")
        
        return evaluation_summary
    
    def save_predictions(self, predictions: List[Tuple[int, List[str], float]], 
                        output_file: str = "predictions.csv"):
        """Save predictions in the required format"""
        
        self.logger.log_info(f"Saving predictions to: {output_file}")
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                # Write header
                f.write("num_correct,answers\n")
                
                # Write predictions
                for idx, answers, _ in predictions:
                    num_correct = len(answers)
                    if num_correct == 0:
                        answers_str = ""
                    elif num_correct == 1:
                        answers_str = answers[0]
                    else:
                        answers_str = f'"{",".join(answers)}"'
                    
                    f.write(f"{num_correct},{answers_str}\n")
            
            self.logger.log_info("Predictions saved successfully")
            
        except Exception as e:
            self.logger.log_error("Failed to save predictions", e)
            raise
    
    def run_complete_evaluation(self, questions_file: str = None, 
                              ground_truth_file: str = None,
                              output_file: str = "predictions.csv",
                              max_workers: int = 1,
                              limit: int = None,
                              random_sampling: bool = False,
                              range_spec: str = None) -> Dict:
        """Run complete evaluation pipeline with GPU optimization"""
        
        # Use default file paths if not provided
        questions_file = questions_file or self.config.QUESTIONS_PATH
        ground_truth_file = ground_truth_file or self.config.TRUE_RESULTS_PATH
        
        self.logger.log_info("Starting complete evaluation pipeline")
        
        # Log system information
        import torch
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0)
            gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
            self.logger.log_info(f"GPU: {gpu_name} ({gpu_memory:.1f}GB)")
        else:
            self.logger.log_info("Running on CPU")
        
        try:
            # Load data with sampling options
            questions_df = self.load_questions(
                questions_file, 
                limit=limit, 
                random_sampling=random_sampling, 
                range_spec=range_spec
            )
            ground_truth = self.load_ground_truth(ground_truth_file)
            
            # Adjust ground truth to match selected questions
            if limit or range_spec:
                if range_spec:
                    start, end = map(int, range_spec.split('-'))
                    ground_truth = ground_truth[start-1:end]
                elif limit:
                    if random_sampling:
                        # For random sampling, we need to match the selected indices
                        selected_indices = questions_df.index.tolist()
                        ground_truth = [ground_truth[i] for i in selected_indices if i < len(ground_truth)]
                    else:
                        ground_truth = ground_truth[:limit]
            
            # Process questions with GPU optimization
            start_time = time.time()
            predictions = self.batch_process_questions(questions_df, max_workers)
            processing_time = time.time() - start_time
            
            self.logger.log_info(f"Total processing time: {processing_time:.2f}s")
            self.logger.log_info(f"Average time per question: {processing_time/len(predictions):.2f}s")
            
            # Log GPU utilization summary
            if torch.cuda.is_available():
                max_memory = torch.cuda.max_memory_allocated() / 1024**3
                self.logger.log_info(f"Peak GPU memory usage: {max_memory:.2f}GB")
                torch.cuda.reset_peak_memory_stats()  # Reset for next run
            
            # Save predictions
            self.save_predictions(predictions, output_file)
            
            # Evaluate results
            evaluation = self.evaluate_results(predictions, ground_truth)
            
            # Save evaluation summary
            eval_summary_file = output_file.replace('.csv', '_evaluation.json')
            import json
            with open(eval_summary_file, 'w', encoding='utf-8') as f:
                json.dump(evaluation, f, ensure_ascii=False, indent=2)
            
            self.logger.log_info(f"Evaluation summary saved to: {eval_summary_file}")
            
            return evaluation
            
        except Exception as e:
            self.logger.log_error("Failed to complete evaluation pipeline", e)
            raise


if __name__ == "__main__":
    # Test the processor
    print("Initializing RAG system...")
    rag_system = VietnameseMCQRAG()
    rag_system.initialize()
    
    print("Creating MCQ processor...")
    processor = MCQProcessor(rag_system)
    
    print("Running evaluation...")
    results = processor.run_complete_evaluation()
    
    print(f"\nFinal Results:")
    print(f"Score: {results['final_score']:.2f}%")
    print(f"Perfect answers: {results['perfect_answers']}")
    print(f"Partial answers: {results['partial_answers']}")
    print(f"Wrong answers: {results['wrong_answers']}")