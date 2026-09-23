\# MediLens: On-Device AI Medical Report Interpreter



MediLens is a fully offline, privacy-first application designed for Snapdragon-powered HP PCs. It translates complex medical jargon from lab reports, prescriptions, and discharge summaries into plain, understandable language using advanced on-device AI. 



By running entirely locally on the Snapdragon NPU and CPU, MediLens ensures that sensitive personal health information (PHI) never leaves the user's machine, eliminating the privacy risks associated with cloud-based LLM APIs.



\## Architecture \& Qualcomm AI Hub Integration



MediLens chains two optimized models from the \*\*Qualcomm AI Hub\*\*, executed natively on Windows ARM64 using the \*\*GenieX SDK\*\*.



1\. \*\*Optical Character Recognition (OCR):\*\* 

&#x20;  - \*\*Model:\*\* `TrOCR` (320x320)

&#x20;  - \*\*Role:\*\* Extracts raw text from uploaded images or PDFs of medical reports.

&#x20;  - \*\*Hardware:\*\* NPU-accelerated (Snapdragon X Elite).

2\. \*\*Semantic Translation \& Q\&A (SLM):\*\* 

&#x20;  - \*\*Model:\*\* `Llama-v3.2-3B-Instruct` (w4a16 quantized, 4096 context)

&#x20;  - \*\*Role:\*\* Processes the extracted text, identifies abnormal values, and explains the results in simple terms. Supports conversational follow-up questions.

&#x20;  - \*\*Hardware:\*\* CPU/NPU hybrid processing.



\## Performance Benchmarks (Snapdragon X Elite)

\* \*\*OCR Latency:\*\* \~2.072 ms 

\* \*\*SLM Generation Rate:\*\* \~12.13 tokens/sec

\* \*\*Time to First Token:\*\* 0.118 sec (short prompt)



\## Repository Structure

\* `/backend/src/` - Core Python inference logic linking TrOCR and Llama-3.2-3B.

\* `/backend/models/` - Configuration and export scripts for AI Hub models.

\* `/demo/` - Sample report images for testing the pipeline.



\## Setup Instructions



\*\*1. Environment Configuration\*\*

Ensure you are running 64-bit AMD Python (required for Windows on Snapdragon X Elite compatibility with these specific toolchains).



pip install -r requirements.txt

pip install qai\_hub\_models



\*\*2. Qualcomm AI Hub Authentication\*\*

Register at the Qualcomm AI Hub and configure your API token:

qai-hub configure --api\_token YOUR\_TOKEN



\*\*3. Model Compilation \& Export\*\*

Export the Llama model optimized for the Snapdragon X Elite CRD:

python -m qai\_hub\_models.models.llama\_v3\_2\_3b\_instruct.export \\

&#x20; --device "Snapdragon X Elite CRD" \\

&#x20; --skip-inferencing --skip-profiling \\

&#x20; --output-dir genie\_bundle



\*(Note: Exporting requires significant memory. If local memory is insufficient, compilation can be completed on the Qualcomm Device Cloud (QDC).)\*



\## Running the Demo

cd backend/src

python main.py --image ../../demo/sample\_report.jpg



\## Author

Shoaib Ahmad

