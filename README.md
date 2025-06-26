# 📄 Chat-with-Documents 🤖

A chatbot application that retrieves information from uploaded PDF documents using LLMs. Built using **LangChain**, **Streamlit**, and **OpenAI**.

---

## 🚀 How to Run the App

Follow the steps below to set up and run the application on your local machine.

### 🔁 Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

📦 Step 1: Create and Activate a Conda Environment
conda create -n genai python=3.10 -y
conda activate genai

📥 Step 2: Install Requirements
pip install -r requirements.txt

🔐 Step 3: Set Up Environment Variables
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

▶️ Step 4: Run the App
streamlit run app.py

Then open your browser and go to:

📍 http://localhost:8501

🛠️ Tech Stack
Python

LangChain

Streamlit

Google PaLM 2

FAISS

pdfplumber / PyPDF2

📂 Features
Upload and parse PDFs 📄

Text chunking for better context management

Conversational memory and context handling

Embedding-based retrieval using FAISS

Real-time chatbot interface using Streamlit
