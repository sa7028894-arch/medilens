# 🩺 MediLens: On-Device AI Medical Report Interpreter__

> **A privacy-first, fully offline application designed for Snapdragon-powered PCs. MediLens translates complex medical jargon from lab reports, prescriptions, and discharge summaries into plain, understandable language.**

By running entirely locally on the Snapdragon NPU and CPU, MediLens ensures that sensitive personal health information (PHI) never leaves the user's machine, eliminating the privacy risks associated with cloud-based AI APIs.

---

## 🏗️ Architecture Flow

```text
 +------------------+       +-------------------+       +-----------------------+
 | 📄 Upload Report |       | 👁️ TrOCR (NPU)    |       | 📝 Extracted Raw Text |
 |  (Image / PDF)   | ----> |  Optical Read     | ----> |  (320x320 resolution) |
 +------------------+       +-------------------+       +-----------+-----------+
                                                                    |
                                                                    v
 +------------------+       +-------------------+       +-----------+-----------+
 | 💡 Plain English |       | 🧠 Llama 3.2 3B   |       | ⚙️ GenieX SDK         |
 |   Explanation    | <---- |  (CPU/NPU Hybrid) | <---- |  Semantic Translation |
 +------------------+       +-------------------+       +-----------------------+
⚙️ Qualcomm AI Hub IntegrationMediLens chains two optimized models from the Qualcomm AI Hub, executed natively on Windows ARM64 using the GenieX SDK:Optical Character Recognition (OCR)Model: TrOCR (320x320)Role: Extracts raw text from uploaded images or PDFs of medical reports.Hardware: NPU-accelerated (Snapdragon X Elite).Semantic Translation & Q&A (SLM)Model: Llama-v3.2-3B-Instruct (w4a16 quantized, 4096 context)Role: Processes the extracted text, identifies abnormal values, and explains the results in simple terms. Supports conversational follow-up questions.Hardware: CPU/NPU hybrid processing.

⚡ Performance Benchmarks (Snapdragon X Elite)

MetricPerformanceOCR Latency~2.072 msSLM Generation Rate~12.13 tokens/secTime to First Token0.118 sec (short prompt)
📂 Repository StructurePlaintext📦 medilens

 ┣ 📂 backend
 ┃ ┣ 📂 src       # Core Python inference logic linking TrOCR and Llama-3.2-3B
 ┃ ┗ 📂 models    # Configuration and export scripts for AI Hub models
 ┣ 📂 demo        # Sample report images for testing the pipeline
 ┣ 📜 app.py      # CustomTkinter Desktop Application interface
 ┗ 📜 README.md   # Project documentation


🚀 Setup & Installation1.

 Environment ConfigurationEnsure you are running 64-bit AMD Python (required for Windows on Snapdragon X Elite compatibility with these specific toolchains).Bashpy -m pip install -r requirements.txt
py -m pip install qai_hub_models

2. Qualcomm AI Hub AuthenticationRegister at the Qualcomm AI Hub and configure your API token:Bashqai-hub configure --api_token YOUR_TOKEN

3. Model Compilation & ExportExport the Llama model optimized for the Snapdragon X Elite CRD:Bashpy -m qai_hub_models.models.llama_v3_2_3b_instruct.export \
  --device "Snapdragon X Elite CRD" \
  --skip-inferencing --skip-profiling \
  --output-dir genie_bundle
(Note: Exporting requires significant memory. If local memory is insufficient, compilation can be completed on the Qualcomm Device Cloud - QDC.)

🎯 Running the Demo

Via Command Line (CLI Pipeline):
Bash
cd backend/src
py main.py --image ../../demo/sample_report.jpg


Via Desktop Application (GUI):

Bash

cd C:\Users\sa702\medilens
py app.py

Author: Shoaib Ahmad
