import customtkinter as ctk
from tkinter import filedialog
import threading

# Import your backend logic
from backend.src.ocr import load_ocr_model, extract_text
from backend.src.llm import load_llm, analyze_report

# Initialize Models (Simulated for startup)
print("Loading AI Models into memory...")
processor, ocr_model = load_ocr_model()
tokenizer = load_llm()

# Configure the Desktop Window
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MediLensApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window settings
        self.title("MediLens - On-Device AI Medical Interpreter")
        self.geometry("800x650")
        
        # Sun/Moon Segmented Button for Theme Toggle (Top Right Corner)
        self.theme_toggle = ctk.CTkSegmentedButton(
            self, 
            values=["☀️", "🌙"], 
            command=self.toggle_mode
        )
        self.theme_toggle.pack(pady=10, padx=20, anchor="ne")
        self.theme_toggle.set("🌙") # Starts in Dark Mode

        # UI Elements
        self.label = ctk.CTkLabel(self, text="MediLens Medical Report Interpreter", font=("Arial", 24, "bold"))
        self.label.pack(pady=10)
        
        self.upload_btn = ctk.CTkButton(self, text="Upload Medical Report (Image)", command=self.upload_image, font=("Arial", 16))
        self.upload_btn.pack(pady=10)
        
        self.status_label = ctk.CTkLabel(self, text="Status: Ready", font=("Arial", 14), text_color="gray")
        self.status_label.pack(pady=10)
        
        self.result_box = ctk.CTkTextbox(self, width=700, height=350, font=("Arial", 14), wrap="word")
        self.result_box.pack(pady=10)
        self.result_box.insert("0.0", "Your plain-language medical explanation will appear here...")
        
        self.image_path = None

    def toggle_mode(self, value):
        # Shifts the entire UI based on which icon is selected
        if value == "🌙":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        
        if self.image_path:
            self.result_box.delete("0.0", "end")
            self.status_label.configure(text=f"Status: Processing {self.image_path.split('/')[-1]}...", text_color="yellow")
            threading.Thread(target=self.process_report).start()

    def process_report(self):
        try:
            self.status_label.configure(text="Status: Extracting text using NPU...")
            extracted_text = extract_text(self.image_path, processor, ocr_model)
            
            self.status_label.configure(text="Status: Analyzing medical terms using GPT-2...")
            explanation = analyze_report(tokenizer, extracted_text)
            
            self.result_box.delete("0.0", "end")
            self.result_box.insert("0.0", f"--- EXTRACTED TEXT ---\n{extracted_text}\n\n--- MEDICAL EXPLANATION ---\n{explanation}")
            self.status_label.configure(text="Status: Analysis Complete (100% On-Device)", text_color="green")
            
        except Exception as e:
            self.result_box.insert("0.0", f"Error: {str(e)}")
            self.status_label.configure(text="Status: Error occurred", text_color="red")

if __name__ == "__main__":
    app = MediLensApp()
    app.mainloop()