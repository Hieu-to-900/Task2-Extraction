from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import sys
import threading
from pynput import keyboard

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


def get_multiline_input(prompt="You: "):
    """
    Get multi-line input from user. Press Enter to add a new line,
    Press Shift+Enter to submit the input.
    """
    lines = []
    shift_pressed = threading.Event()
    submit_flag = threading.Event()
    listener = None
    
    def on_press(key):
        try:
            # Check if Shift is pressed
            if key == keyboard.Key.shift or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                shift_pressed.set()
        except AttributeError:
            pass
    
    def on_release(key):
        try:
            # Check if Enter is pressed while Shift is held
            if key == keyboard.Key.enter and shift_pressed.is_set():
                submit_flag.set()
                return False  # Stop listener
            # Reset shift flag when Shift is released
            if key == keyboard.Key.shift or key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                shift_pressed.clear()
        except AttributeError:
            pass
    
    # Start keyboard listener in a separate thread
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    
    try:
        # Print initial prompt
        print(f"\n{prompt}", end="", flush=True)
        
        # Read lines until Shift+Enter is pressed
        while not submit_flag.is_set():
            try:
                # Read a line (this will block until Enter is pressed)
                line = sys.stdin.readline()
                
                # Check if Shift+Enter was pressed (check immediately after reading)
                if submit_flag.is_set():
                    # Shift+Enter was pressed, don't add this line
                    break
                
                # Remove trailing newline
                if line.endswith('\n'):
                    line = line[:-1]
                
                # Add line to collection
                lines.append(line)
                
                # If it's a regular Enter (not Shift+Enter), continue to next line
                # Print continuation prompt for next line
                if not submit_flag.is_set():
                    print("  ", end="", flush=True)  # Indent for continuation
                
            except (EOFError, KeyboardInterrupt):
                break
        
        # Join all lines
        result = '\n'.join(lines).strip()
        return result
        
    finally:
        # Stop and cleanup listener
        if listener and listener.is_alive():
            listener.stop()
            listener.join(timeout=0.1)


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
    print("Multi-line input: Press Enter to add a new line, Shift+Enter to submit")
    print("=" * 50)

    while True:
        try:
            user_input = get_multiline_input()
            
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
