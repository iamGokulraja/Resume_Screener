# 📄 Resume Rank AI - Resume Screening & Ranking System

A simple AI-powered Resume Screening and Ranking System built using **Python + Streamlit**.

This project automatically:

* Reads resumes from a folder
* Extracts text from PDF resumes
* Reads Job Description
* Calculates similarity score
* Ranks resumes
* Displays an interactive dashboard UI
* Allows downloading ranking results as CSV

---

## 🚀 Features

✅ Resume PDF Reading

✅ Job Description Matching

✅ Resume Ranking

✅ Match Percentage

✅ Dashboard UI

✅ Hover Glow Cards

✅ Progress Bars

✅ Ranking Chart

✅ Folder-Based Processing

✅ Download Ranking as CSV

✅ Deployable on Streamlit Community Cloud

---

## 🖼️ Project Output

```plaintext
📄 Resume Ranking Dashboard

Total Resume : 6
Highest Match : 18%

🏆 Resume Ranking

1 Resume1 18%
2 Resume2 16%
3 Resume3 14%

⬇ Download CSV

✨ Match Dashboard

📄 Resume1
18%
🟢 Strong

📄 Resume2
16%
🟡 Medium

📄 Resume3
14%
🔴 Low

📊 Ranking Chart
```

---

## 📂 Project Structure

```plaintext
Resume_Screener/

│── app.py

│── requirements.txt

│── README.md

│── data/

│   ├── resumes/

│   │     ├── resume1.pdf

│   │     ├── resume2.pdf

│   │     └── resume3.pdf

│   │

│   └── job_description.txt
```

---

## ⚙️ Installation

Clone repository

```bash
git clone <your_repo_url>
```

Move into project

```bash
cd Resume_Screener
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
streamlit run app.py
```

Open browser:

```plaintext
http://localhost:8501
```

---

## 🧠 How It Works

```plaintext
Resume PDFs
      ↓
Extract Text
      ↓
TF-IDF
(Text → Numeric Vector)
      ↓
Cosine Similarity
      ↓
Calculate Match %
      ↓
Resume Ranking
      ↓
Download CSV
      ↓
Dashboard UI
```

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* PDFPlumber
* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity

---

## 📊 Algorithm

### TF-IDF

Converts text into numeric vectors.

Example:

```plaintext
Python SQL

↓

[0.6, 0.8]
```

### Cosine Similarity

Measures similarity between:

```plaintext
Job Description

VS

Resume
```

Output:

```plaintext
18%
```

---

## 🎯 Future Improvements

* Resume Upload UI
* OCR Support
* Export Excel
* Resume Summary
* AI Recommendations
* Skill Extraction

---

## 👨‍💻 Author

**Gokul Raja**

Built with ❤️ using Python & Streamlit
