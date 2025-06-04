# 🤖 Smart Resume Analyzer AI

An AI-powered tool that analyzes resumes and extracts 20+ structured insights using GPT-3.5/GPT-4. Perfect for HR tech, resume screening, or job matching applications.

> 📄 Built on LangChain + OpenAI + PDF parsing with advanced prompt engineering.

---

## 🚀 What It Does

Upload one or more PDF resumes and get:
- 🎯 Education, skills, certifications, and job history
- 📊 AI-powered suitability rating for selected job roles
- 📁 Export as Excel or CSV (HR-friendly format)
- 🧠 GPT-based content extraction and structuring

---

## ✨ Features

- ✅ Resume parsing via OCR (PDF support)
- ✅ GPT-driven information extraction (23 fields)
- ✅ Excel/CSV output with clean structure
- ✅ Job-role-based scoring and suitability analysis
- ✅ Automatically chooses GPT-3.5 or GPT-4 based on token size
- ✅ Customizable prompt for different use-cases

---

## 🛠 Technologies Used

- Python 3.8+
- LangChain
- OpenAI GPT-3.5 / GPT-4 API
- PyMuPDF / pdfminer / Tesseract OCR
- Pandas for Excel output
- Streamlit (optional if you add UI)

---

## 🧠 What I Added / Customized

✅ Rewrote prompt logic to include job-fit analysis  
✅ Added support for uploading job descriptions and matching against resume  
✅ Improved error handling for GPT-4 rate limits  
✅ Designed scoring system based on keyword matching  
✅ Refactored folder structure for clarity  
✅ Deployed version with sample resume + JD for demo

---

## Sample Output

| Field                    | Example           |
| ------------------------ | ----------------- |
| Education Bachelor Major | Computer Science  |
| Top 3 Technical Skills   | Python, SQL, AWS  |
| Experience Companies     | \[Google, Aptean] |
| Suitable Position        | Backend Engineer  |
| Candidate Rating         | 8.5 / 10          |
