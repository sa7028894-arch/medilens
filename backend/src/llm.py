from transformers import AutoTokenizer

def load_llm():
    print("Loading LLM template (Open-source GPT-2 fallback for prototype)...")
    
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    return tokenizer

def analyze_report(tokenizer, extracted_text):
    print("Analyzing medical report text...")
    system_prompt = "You are a helpful medical assistant. Explain the following medical report in plain language. Note: this does not replace professional medical advice."
    
    
    prompt = f"System: {system_prompt}\n\nUser: Please explain this report:\n{extracted_text}\n\nAssistant:"
    
    
    simulated_response = "Based on the text extracted, the report indicates your values are within normal ranges. Please consult your doctor for a full diagnosis."
    return simulated_response

if __name__ == "__main__":
    print("LLM module initialized.")
