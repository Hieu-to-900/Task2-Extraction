"""
Main Runner Script for Vietnamese MCQ RAG System
Command line interface for running the complete pipeline
"""

import argparse
import os
import sys
import json
from datetime import datetime

from rag_system import VietnameseMCQRAG, RAGConfig
from mcq_processor import MCQProcessor, DebugSession


def print_banner():
    """Print system banner"""
    banner = """
╔══════════════════════════════════════════════════════════════════╗
║                Vietnamese MCQ RAG System                         ║
║               Retrieval-Augmented Generation                     ║
║          for Multiple Choice Question Answering                  ║
╚══════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def check_files_exist(config: RAGConfig):
    """Check if required files exist"""
    files_to_check = [
        (config.DOCUMENT_PATH, "Document file"),
        (config.QUESTIONS_PATH, "Questions file"),
        (config.TRUE_RESULTS_PATH, "Ground truth file")
    ]
    
    missing_files = []
    for file_path, description in files_to_check:
        if not os.path.exists(file_path):
            missing_files.append(f"{description}: {file_path}")
    
    if missing_files:
        print("❌ Missing required files:")
        for missing in missing_files:
            print(f"   - {missing}")
        return False
    
    print("✅ All required files found")
    return True


def print_system_info():
    """Print system information"""
    print("\n📋 System Configuration:")
    print(f"   Embedding Model: {RAGConfig.EMBEDDING_MODEL}")
    print(f"   Generation Model: {RAGConfig.GENERATION_MODEL}")
    print(f"   Top-K Retrieval: {RAGConfig.TOP_K}")
    print(f"   Chunk Size: {RAGConfig.CHUNK_SIZE}")
    print()


def run_debug(args):
    """Run interactive debug mode for multiple questions"""
    
    print_banner()
    print("🐛 INTERACTIVE DEBUG MODE")
    print("="*60)
    
    config = RAGConfig()
    
    # Override config with command line arguments
    if args.document:
        config.DOCUMENT_PATH = args.document
    if args.questions:
        config.QUESTIONS_PATH = args.questions
    if args.ground_truth:
        config.TRUE_RESULTS_PATH = args.ground_truth
    
    try:
        print("🚀 Initializing RAG system...")
        rag_system = VietnameseMCQRAG(config)
        rag_system.initialize()
        
        print("🔄 Creating debug session...")
        debug_session = DebugSession(rag_system)
        
        if not debug_session.initialize():
            return 1
        
        # Debug first question from command line
        current_question_id = args.question_id
        print(f"\n🐛 Debugging question {current_question_id}...")
        debug_session.debug_question(current_question_id)
        
        # Interactive loop for additional questions
        while True:
            print("\n" + "🔄" + "="*79)
            print("Enter next question ID to debug (or 'q'/'quit' to exit):")
            print(f"Valid range: 1-{debug_session.total_questions}")
            
            try:
                user_input = input("Question ID: ").strip().lower()
                
                # Check for quit commands
                if user_input in ['q', 'quit', 'exit']:
                    print("👋 Exiting debug session. Goodbye!")
                    break
                
                # Validate and convert to integer
                try:
                    question_id = int(user_input)
                except ValueError:
                    print(f"❌ Invalid input '{user_input}'. Please enter a number or 'q' to quit.")
                    continue
                
                # Debug the question
                print(f"\n🐛 Debugging question {question_id}...")
                debug_session.debug_question(question_id)
                
            except KeyboardInterrupt:
                print("\n\n👋 Debug session interrupted. Exiting...")
                break
            except EOFError:
                print("\n\n👋 Input stream ended. Exiting...")
                break
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error during debug: {str(e)}")
        return 1


def run_evaluation(args):
    """Run the complete evaluation pipeline"""
    
    print_banner()
    print_system_info()
    
    # Create config
    config = RAGConfig()
    
    # Override config with command line arguments
    if args.document:
        config.DOCUMENT_PATH = args.document
    if args.questions:
        config.QUESTIONS_PATH = args.questions
    if args.ground_truth:
        config.TRUE_RESULTS_PATH = args.ground_truth
    if args.top_k:
        config.TOP_K = args.top_k
    
    # Set performance mode
    if args.quick:
        config.TOP_K = 1
        config.QUICK_MODE = True
    elif args.accurate:
        config.TOP_K = 5
        config.ACCURATE_MODE = True
    
    # Check files
    if not check_files_exist(config):
        return 1
    
    try:
        print("🚀 Initializing RAG system...")
        rag_system = VietnameseMCQRAG(config)
        rag_system.initialize(force_rebuild_index=args.rebuild_index)
        
        print("🔄 Creating MCQ processor...")
        processor = MCQProcessor(rag_system)
        
        print("📝 Running evaluation pipeline...")
        start_time = datetime.now()
        
        results = processor.run_complete_evaluation(
            questions_file=config.QUESTIONS_PATH,
            ground_truth_file=config.TRUE_RESULTS_PATH,
            output_file=args.output,
            max_workers=args.workers,
            limit=args.limit,
            random_sampling=args.random,
            range_spec=args.range
        )
        
        end_time = datetime.now()
        total_time = (end_time - start_time).total_seconds()
        
        # Print results summary
        print("\n" + "="*60)
        print("📊 EVALUATION RESULTS")
        print("="*60)
        print(f"🎯 Final Score: {results['final_score']:.2f}%")
        print(f"📊 Total Questions: {results['total_questions']}")
        print(f"✅ Perfect Answers: {results['perfect_answers']}")
        print(f"⚠️  Partial Answers: {results['partial_answers']}")
        print(f"❌ Wrong Answers: {results['wrong_answers']}")
        print(f"⏱️  Average Processing Time: {results['average_processing_time']:.2f}s per question")
        print(f"🕐 Total Runtime: {total_time:.2f}s")
        print("="*60)
        
        # Performance breakdown
        if results['total_questions'] > 0:
            perfect_rate = (results['perfect_answers'] / results['total_questions']) * 100
            partial_rate = (results['partial_answers'] / results['total_questions']) * 100
            wrong_rate = (results['wrong_answers'] / results['total_questions']) * 100
            
            print("\n📈 Performance Breakdown:")
            print(f"   Perfect answers: {perfect_rate:.1f}%")
            print(f"   Partial answers: {partial_rate:.1f}%")
            print(f"   Wrong answers: {wrong_rate:.1f}%")
        
        # File locations
        print(f"\n📁 Output Files:")
        print(f"   Predictions: {args.output}")
        print(f"   Evaluation: {args.output.replace('.csv', '_evaluation.json')}")
        print(f"   Logs: rag_system.log")
        
        # Performance rating
        score = results['final_score']
        if score >= 90:
            rating = "🏆 Excellent"
        elif score >= 80:
            rating = "🥇 Very Good"
        elif score >= 70:
            rating = "🥈 Good"
        elif score >= 60:
            rating = "🥉 Fair"
        else:
            rating = "💭 Needs Improvement"
        
        print(f"\n🎖️  Performance Rating: {rating}")
        print("\n✅ Evaluation completed successfully!")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error during evaluation: {str(e)}")
        print("Check the log file for detailed error information.")
        return 1


def run_single_test(args):
    """Run a single question test"""
    
    print_banner()
    
    config = RAGConfig()
    if args.document:
        config.DOCUMENT_PATH = args.document
    
    try:
        print("🚀 Initializing RAG system...")
        rag_system = VietnameseMCQRAG(config)
        rag_system.initialize()
        
        # Interactive question input
        print("\n📝 Enter your question:")
        question = input("Question: ")
        
        print("\nEnter options:")
        options = {}
        for letter in ['A', 'B', 'C', 'D']:
            option = input(f"Option {letter}: ")
            options[letter] = option
        
        print(f"\n🔍 Processing question...")
        start_time = datetime.now()
        
        answers = rag_system.answer_mcq(question, options)
        
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds()
        
        print(f"\n📋 Results:")
        print(f"Question: {question}")
        print(f"Predicted Answers: {', '.join(answers) if answers else 'None'}")
        print(f"Processing Time: {processing_time:.2f}s")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return 1


def main():
    """Main entry point"""
    
    parser = argparse.ArgumentParser(
        description="Vietnamese MCQ RAG System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full evaluation
  python main.py evaluate

  # Run with custom files
  python main.py evaluate --questions my_questions.csv --ground-truth my_results.md

  # Rebuild index and run evaluation
  python main.py evaluate --rebuild-index

  # Test single question interactively
  python main.py test --rebuild-index

  # Debug specific question
  python main.py debug 3
  # Then interactively debug more questions: 5, 10, q

  # Run with more parallel workers
  python main.py evaluate --workers 4
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Evaluate command
    eval_parser = subparsers.add_parser('evaluate', help='Run complete evaluation')
    eval_parser.add_argument('--document', '-d', 
                           help='Path to document file')
    eval_parser.add_argument('--questions', '-q',
                           help='Path to questions CSV file')
    eval_parser.add_argument('--ground-truth', '-g',
                           help='Path to ground truth file')
    eval_parser.add_argument('--output', '-o',
                           default='predictions.csv',
                           help='Output predictions file')
    eval_parser.add_argument('--rebuild-index', 
                           action='store_true',
                           help='Force rebuild vector index')
    eval_parser.add_argument('--top-k', type=int,
                           help='Number of top documents to retrieve')
    eval_parser.add_argument('--workers', type=int, default=1,
                           help='Number of parallel workers for processing')
    
    # Limited testing options
    eval_parser.add_argument('--limit', type=int,
                           help='Test only first N questions')
    eval_parser.add_argument('--random', action='store_true',
                           help='Use random sampling instead of first N questions')
    eval_parser.add_argument('--range', type=str,
                           help='Test specific range (e.g., "100-200")')
    
    # Performance modes
    eval_parser.add_argument('--quick', action='store_true',
                           help='Quick mode: faster but less accurate')
    eval_parser.add_argument('--accurate', action='store_true',
                           help='Accurate mode: slower but more accurate')
    
    # Test command
    test_parser = subparsers.add_parser('test', help='Test with single question')
    test_parser.add_argument('--document', '-d',
                           help='Path to document file')
    
    # Debug command
    debug_parser = subparsers.add_parser('debug', help='Debug specific question interactively')
    debug_parser.add_argument('question_id', type=int, help='Initial question ID to debug (1-based)')
    debug_parser.add_argument('--document', '-d',
                            help='Path to document file')
    debug_parser.add_argument('--questions', '-q',
                            help='Path to questions CSV file')
    debug_parser.add_argument('--ground-truth', '-g',
                            help='Path to ground truth file')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    if args.command == 'evaluate':
        return run_evaluation(args)
    elif args.command == 'test':
        return run_single_test(args)
    elif args.command == 'debug':
        return run_debug(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())