#!/usr/bin/env python3
import os
import time
import pandas as pd
import google.generativeai as genai
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("❌ Error: GEMINI_API_KEY environment variable not set.")
    exit(1)

genai.configure(api_key=API_KEY)
EXCEL_FILE = "document_annotations.xlsx"
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=["Title", "Label", "Text", "Encoding"])
    df.to_excel(EXCEL_FILE, index=False)
    print(f"✅ Created new Excel file: {EXCEL_FILE}")
def get_gemini_response(prompt, document_text=""):
    model = genai.GenerativeModel("gemini-pro")
    
    for attempt in range(3):
        try:
            response = model.generate_content(prompt + "\n\n" + document_text if document_text else prompt)
            return response.text.strip() if response and response.text else "N/A"
        except Exception as e:
            print(f"⚠️ API Error: {e}")
            if "429" in str(e):
                print("⚠️ Rate limit reached, waiting 10 seconds...")
                time.sleep(10)
            else:
                return "Error"
    return "Error"
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text if text else "No text found in PDF"
    except Exception as e:
        print(f"❌ Error extracting text from {pdf_path}: {e}")
        return "Error"
def encode_text(text):
    try:
        vectorizer = TfidfVectorizer()
        encoding_matrix = vectorizer.fit_transform([text])
        encoding_array = encoding_matrix.toarray()
        return encoding_array.tolist()[0]
    except Exception as e:
        print(f"❌ Error encoding text: {e}")
        return []
def process_files_in_folder(base_directory):
    if not os.path.exists(base_directory):
        print(f"❌ Error: Directory '{base_directory}' does not exist.")
        return

    for root, _, files in os.walk(base_directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                print(f"📄 Processing: {file}")

                document_text = extract_text_from_pdf(pdf_path)
                if document_text == "Error":
                    continue

                label_prompt = "Assign a category: Deep Learning, Computer Vision, Reinforcement Learning, NLP, Optimization etc."
                document_label = get_gemini_response(label_prompt, document_text[:2000])

                encoding = encode_text(document_text)

                new_row = {
                    "Title": file,
                    "Label": document_label,
                    "Text": document_text,
                    "Encoding": str(encoding)
                }
                df = pd.read_excel(EXCEL_FILE)
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df.to_excel(EXCEL_FILE, index=False)

                print(f"✅ Processed: {file}\n")
if __name__ == "__main__":
    base_directory = os.path.join(os.getcwd(), "new")
    process_files_in_folder(base_directory)
