“I have done this process on linux using virtual environment. The process to install the tools etc. might be different for Windows and Mac but the libraries required to run it are the same”
Paper Crawler
📌 Overview
This script is a Scrapy-based web crawler that scrapes research papers from the NeurIPS (NIPS) conference website, extracts their metadata, downloads PDF files, and saves them into structured directories. The extracted data is optionally saved in an Excel file (papers.xlsx).
⚙️ Features
Crawls the NeurIPS (NIPS) papers website.
Extracts paper titles and their corresponding PDF links.
Downloads the research papers in structured year-wise folders.
Saves metadata (title and abstract) into an Excel file (papers.xlsx).
🛠 Prerequisites
Ensure you have the following installed:
1️⃣ Install Python (if not already installed)
This script requires Python 3.7+. Check your Python version:
python3 --version

2️⃣ Create & Activate a Virtual Environment (Recommended)
python3 -m venv CrawlerENV
source CrawlerENV/bin/activate  # For Linux/Mac
CrawlerENV\Scripts\activate    # For Windows

3️⃣ Install Required Libraries
Inside your virtual environment, install dependencies:
pip install scrapy pandas openpyxl


📌 How to Use
1️⃣ Run the script:
python paper_crawler.py

2️⃣ Wait for the process to complete.
3️⃣ The results will be stored as:
PDF files in directories structured by year (/YYYY/Paper_Title.pdf)
Metadata in papers.xlsx (Title & Abstract)

📊 Expected Output
The script downloads research papers and stores them as follows:
Folder structure:
 📂 2023
  ├── paper1.pdf
  ├── paper2.pdf
📂 2022
  ├── paper3.pdf
  ├── paper4.pdf


Excel File (papers.xlsx) Format:
Title
Abstract
Paper Name
Abstract Text


⚠️ Common Issues & Fixes
1️⃣ Scrapy Not Installed
If you see:
ModuleNotFoundError: No module named 'scrapy'

Install it using:
pip install scrapy

2️⃣ Website Structure Changes
If the website changes its structure, some CSS selectors may stop working. In that case:
Inspect the website’s HTML (Ctrl+Shift+I in Chrome) and update parsePapers() accordingly.
3️⃣ Missing Abstracts
If abstracts are not extracted correctly:
Uncomment the abstract extraction code in parsePapers().
Adjust the CSS selectors accordingly.

✅ Conclusion
This Paper Crawler automates the process of fetching and organizing research papers from NeurIPS. It is useful for researchers, students, and ML enthusiasts who want to bulk-download and analyze research papers efficiently.
🚀 Happy Crawling! If you face issues, tweak the script based on the latest website structure.

Document Annotator
📌 Overview
This script processes PDF documents, extracts text, assigns categories using the Gemini AI API, and generates numerical text encodings using TF-IDF. The processed data is saved in an Excel file (document_annotations.xlsx).
⚙️ Features
Extracts full text from PDF files.
Categorizes documents into relevant fields (e.g., NLP, Computer Vision, Deep Learning, etc.) using the Gemini AI API.
Encodes the extracted text into numerical vectors using TF-IDF.
Saves the results in an Excel file (document_annotations.xlsx).
🛠 Prerequisites
Ensure you have the following installed:
1️⃣ Install Python (if not already installed)
This script requires Python 3.7+. Check your Python version:
python3 --version

2️⃣ Create & Activate a Virtual Environment (Recommended)
python3 -m venv ScraperENV
source ScraperENV/bin/activate  # For Linux/Mac
ScraperENV\Scripts\activate    # For Windows

3️⃣ Install Required Libraries
Inside your virtual environment, install dependencies:
pip install pandas google-generativeai PyPDF2 scikit-learn openpyxl

4️⃣ Set Up Gemini API Key
You need an API key from Google Gemini. Export it as an environment variable:
export GEMINI_API_KEY="your-api-key-here"

For permanent use, add the export command to ~/.bashrc or ~/.zshrc.

📌 How to Use
1️⃣ Place all PDF files inside a folder named new inside your working directory.
2️⃣ Run the script:
python annotator.py

3️⃣ The output will be stored in document_annotations.xlsx.

📊 Expected Output
The Excel file will contain the following columns:
Title → Name of the PDF file.
Label → Category assigned by the Gemini API.
Text → Extracted full text from the PDF.
Encoding → Numerical encoding using TF-IDF.

⚠️ Common Issues & Fixes
1️⃣ ModuleNotFoundError (Missing Dependencies)
If you see an error like:
ModuleNotFoundError: No module named 'sklearn'

Ensure you installed dependencies inside the virtual environment:
pip install pandas google-generativeai PyPDF2 scikit-learn openpyxl

2️⃣ GEMINI_API_KEY Not Set
If you see:
❌ Error: GEMINI_API_KEY environment variable not set.

Make sure you’ve set your API key using:
export GEMINI_API_KEY="your-api-key-here"

3️⃣ Empty or Corrupted PDFs
If a PDF has no text or is scanned, the script may fail to extract text. Consider using an OCR tool like Tesseract:
sudo apt install tesseract-ocr


✅ Conclusion
This script automates document annotation using AI and NLP techniques. It helps researchers, students, and professionals quickly categorize and analyze PDFs efficiently.
🚀 Happy coding! If you encounter any issues, feel free to debug based on the logs or tweak the script as needed!
Github:Automating Research Paper Scraping and Annotation with Python
Medium: Automating Research Paper Scraping and Annotation with Python
