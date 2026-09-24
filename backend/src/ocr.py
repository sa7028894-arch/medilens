from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

def load_ocr_model():
    print("Loading TrOCR model...")
    # Loading the base model for prototyping
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-small-printed')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-small-printed')
    return processor, model

def extract_text(image_path, processor, model):
    print(f"Extracting text from {image_path}...")
    try:
        image = Image.open(image_path).convert("RGB")
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        return generated_text
    except Exception as e:
        return f"Error processing image: {str(e)}"

if __name__ == "__main__":
    print("OCR module initialized.")