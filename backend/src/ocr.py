import argparse
import os
from ocr import load_ocr_model, extract_text
from llm import load_llm, analyze_report

def main():
    parser = argparse.ArgumentParser(description="MediLens AI Medical Report Interpreter")
    parser.add_argument("--image", type=str, required=True, help="Path to the medical report image")
    args = parser.parse_args()

    if not os.path.exists(args.image):
        print(f"Error: Could not find image at {args.image}")
        return

    print("--- Starting MediLens Pipeline ---")
    
   
    processor, ocr_model = load_ocr_model()
    tokenizer = load_llm()
    
   
    extracted_text = extract_text(args.image, processor, ocr_model)
    print(f"\n[Extraction Complete]\nExtracted Text Preview: {extracted_text[:150]}...\n")
    
    
    explanation = analyze_report(tokenizer, extracted_text)
    print(f"[Analysis Complete]\nExplanation: {explanation}\n")
    
    print("--- Pipeline Finished ---")

if __name__ == "__main__":
    main()
