# VAERS LLM

A simple app to download VAERS data, store it in a SQLite database, and query it using natural language with xAI's Grok model via a Gradio interface.

## Prerequisites
- Python 3.8+ (download from python.org)
- Git (download from git-scm.com)
- An xAI API key (get one at https://x.ai/api)
- ~1–2 GB disk space for VAERS data

## Setup
1. **Clone the repo**:
   ```bash
   git clone <https://github.com/medicinalsheep/VAERS-LLM-0.0 >
   cd vaers-llm
   
2. **Install dependencies**:
   ```bash
    pip install -r requirements.txt
   
3. **Download VAERS data:Run the download script (this may take a while due to large file sizes)**:
   ```bash
   python download_data.py

4. **Set up the database:Load the data into a SQLite database**:
   ```bash
   python setup_database.py

5. **Run the app:Start the Gradio interface**:
   ```bash
   python app.py

6. **Use the app:
   -Open the link shown in the terminal (e.g., http://127.0.0.1:7860) in your browser.
   -Enter your xAI API key (it will be saved for future use).
   -Ask questions like:
      -"How many death reports for COVID vaccines in 2021?"
      -"What are the top symptoms for females under 18?"

**NotesVAERS data: The dataset is large, so downloading and setting up the database may take time.
**VAERS limitations: Reports are unverified and do not prove causation.
**Troubleshooting:If you get errors, ensure your API key is valid or re-run pip install -r requirements.txt.
Check your internet connection if downloads are slow.
If the Gradio link doesn't work, try a different browser or check your firewall.

API key: Get it from https://x.ai/api. For help, see the xAI API documentation.

Example Questions"How many reports mention death after COVID vaccines in 2021?"
"What are the most common symptoms for children under 18?"
"Show reports for males over 65 in 2020."

LicenseThis project is for personal use and provided as-is. VAERS data is public domain, but ensure compliance with HHS usage guidelines.

