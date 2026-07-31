# 🚀 Resume Skills & Keywords Extractor using LangGraph + Groq

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-AI-success?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

</p>

---

# 📌 Project Overview

This project is an **ATS Resume Skills & Keywords Extractor** built using **LangGraph**, **LangChain**, and **Groq LLM**.

The application analyzes a **Resume** or **Job Description** and extracts **only the skills and keywords explicitly mentioned** in the text.

Unlike AI-based inference systems, this project **does not generate or predict additional skills**. It extracts only the information present in the input.

---

# ✨ Features

* ✅ Exact Skills Extraction
* ✅ Exact Keywords Extraction
* ✅ Uses LangGraph Workflow
* ✅ Uses Groq Llama 3.3 70B Model
* ✅ Generates Workflow Image (`graph.png`)
* ✅ Step-by-Step Terminal Execution
* ✅ Removes Duplicate Skills
* ✅ ATS-Friendly Output

---

# 🛠 Technologies Used

| Technology       | Purpose               |
| ---------------- | --------------------- |
| 🐍 Python        | Programming Language  |
| 🧠 LangGraph     | Workflow Management   |
| 🔗 LangChain     | Prompt Chaining       |
| ⚡ Groq API       | Large Language Model  |
| 🔐 python-dotenv | Environment Variables |

---

# 📂 Project Structure

```text
Resume-Skills-Extractor/
│
├── main.py
├── .env
├── requirements.txt
├── graph.png
└── README.md
```

---

# ⚙ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Resume-Skills-Extractor.git

cd Resume-Skills-Extractor
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / Mac**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install langgraph
pip install langchain
pip install langchain-groq
pip install python-dotenv
pip install graphviz
```

---

### 4️⃣ Create `.env`

```text
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🖥 Example Input

```text
Python Developer with experience in Python, FastAPI, SQLAlchemy, MySQL, Docker, Git, LangChain, LangGraph and REST API Development.
```

---

# 📤 Example Output

```text
Skills:
- Python
- FastAPI
- SQLAlchemy
- MySQL
- Docker
- Git
- LangChain
- LangGraph

Keywords:
- Python Developer
- REST API Development
```

---

# 🔄 LangGraph Workflow

```mermaid
graph TD

A(Start)
-->B[Read Resume]

B-->C[Extract Skills]

C-->D[Generate Output]

D-->E(End)
```

---

# 💻 Terminal Execution

```text
==================================================
      Resume Skills Extractor
==================================================

Graph saved as graph.png

Enter Resume or Job Description

Python Developer with experience in Python...

==============================
Step 1 : Extracting Skills...
==============================

✓ Extraction Completed

==============================
Extraction Result
==============================

Skills:
- Python
- FastAPI
- SQLAlchemy
- MySQL
- Docker
- Git
- LangChain
- LangGraph

Keywords:
- Python Developer
- REST API Development
```

---

# 📊 Output

The project generates:

* 📄 Skills List
* 📄 Keywords List
* 🖼 Workflow Image (`graph.png`)

---

# 📦 Requirements

```text
langgraph
langchain
langchain-groq
python-dotenv
graphviz
```

---

# 📈 Future Improvements

* 📄 PDF Resume Upload
* 📑 DOCX Resume Support
* 🌐 Streamlit Web Interface
* ⚡ FastAPI REST API
* 📊 Export Results to CSV
* 📁 Export Results to JSON

---

# 👨‍💻 Author

**Jonnadula Naga Samba Siva Rao**

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and share it with others!

**Happy Coding! 🚀**
