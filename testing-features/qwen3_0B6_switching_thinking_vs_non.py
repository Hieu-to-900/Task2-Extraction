from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class QwenChatbot:
    def __init__(self, model_name="Qwen/Qwen3-0.6B"):
        # Check if CUDA is available and set device
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if self.device.type == "cuda" else torch.float32,
            device_map="auto" if self.device.type == "cuda" else None
        )
        
        # Move model to device if not using device_map
        if self.device.type == "cuda" and not hasattr(self.model, 'hf_device_map'):
            self.model = self.model.to(self.device)
            
        self.history = []

    def generate_response(self, user_input):
        messages = self.history + [{"role": "user", "content": user_input}]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            response_ids = self.model.generate(
                **inputs, 
                max_new_tokens=32768,
                do_sample=True,
                temperature=0.7,
                pad_token_id=self.tokenizer.eos_token_id
            )[0][len(inputs.input_ids[0]):].tolist()
            
        response = self.tokenizer.decode(response_ids, skip_special_tokens=True)

        # Update history
        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": response})

        return response

# Example Usage
if __name__ == "__main__":
    chatbot = QwenChatbot()

    # # First input (without /think or /no_think tags, thinking mode is enabled by default)
    # user_input_1 = "How many r's in strawberries?"
    # print(f"User: {user_input_1}")
    # response_1 = chatbot.generate_response(user_input_1)
    # print(f"Bot: {response_1}")
    # print("----------------------")

    # # Second input with /no_think
    # user_input_2 = "Then, how many r's in blueberries? /no_think"
    # print(f"User: {user_input_2}")
    # response_2 = chatbot.generate_response(user_input_2)
    # print(f"Bot: {response_2}") 
    # print("----------------------")

    # # Third input with /think
    # user_input_3 = "Really? /think"
    # print(f"User: {user_input_3}")
    # response_3 = chatbot.generate_response(user_input_3)
    # print(f"Bot: {response_3}")

    # Interactive shell loop
    print("Qwen Chatbot - Interactive Mode")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Use /think or /no_think tags to control thinking mode")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
                
            if not user_input:
                continue
                
            response = chatbot.generate_response(user_input)
            print(f"Bot: {response}")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
