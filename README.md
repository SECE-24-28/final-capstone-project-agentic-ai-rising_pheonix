[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/s7J27iqd)




# 🛡️ Agentic AI Powered Spam Detection System

An intelligent multi-agent AI system that detects spam messages, phishing attempts, and suspicious text using Machine Learning and Large Language Models (LLMs).

---

# 📌 Project Overview

Spam messages, phishing emails, and online scams are increasing rapidly. Traditional spam filters only classify messages as spam or not spam without explaining the reason behind the prediction.

This project introduces an **Agentic AI-based Spam Detection System** that combines:

* Machine Learning
* Natural Language Processing (NLP)
* Large Language Models (LLMs)
* Multi-Agent AI Architecture

The system not only detects spam but also explains:

* why the message is suspicious,
* threat category,
* confidence score,
* phishing indicators.

---

# 🎯 Objectives

* Detect spam and phishing messages accurately
* Use Machine Learning for classification
* Integrate AI agents for intelligent reasoning
* Provide explainable AI outputs
* Build a user-friendly dashboard
* Learn Agentic AI concepts practically

---

# 🚀 Features

✅ Spam Detection
✅ Phishing Detection
✅ Confidence Score
✅ Explainable AI Output
✅ Multi-Agent Workflow
✅ Real-Time Text Analysis
✅ Frontend Dashboard
✅ API-Based Architecture
✅ Local LLM Integration using Ollama

---

# 🧠 Agentic AI Architecture

The system uses multiple AI agents working together.

## 🔹 Input Agent

* Receives user messages
* Cleans and preprocesses text
* Extracts important features

---

## 🔹 Detection Agent

* Uses Machine Learning model
* Predicts spam probability

---

## 🔹 Threat Analysis Agent

* Uses LLM reasoning
* Explains suspicious patterns
* Detects phishing tactics

---

## 🔹 Decision Agent

* Combines ML score + AI reasoning
* Produces final verdict

---

# 🏗️ System Workflow

```text
User Input
   ↓
Input Agent
   ↓
Spam Detection Agent
   ↓
Threat Analysis Agent
   ↓
Decision Agent
   ↓
Frontend Dashboard
```

---

# 🛠️ Tech Stack

## Frontend

* Streamlit

## Backend

* FastAPI

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Naive Bayes

## Agentic AI

* LangChain
* Ollama
* Llama3

## Programming Language

* Python

---

# 📂 Project Structure

```text
spam-detection-system/
│
├── backend/
│   ├── agents/
│   ├── api/
│   ├── model/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── dataset/
│   └── spam.csv
│
├── notebooks/
│   └── train_model.py
│
├── saved_models/
│
├── requirements.txt
│
└── README.md
```

---

# 📊 Dataset

Dataset Used:

* SMS Spam Collection Dataset

Source:

* Kaggle
* UCI Machine Learning Repository

Dataset contains:

* Spam messages
* Normal messages (Ham)

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/spam-detection-system.git
```

---

## 2. Navigate to Project Folder

```bash
cd spam-detection-system
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Libraries

```bash
pip install pandas scikit-learn fastapi uvicorn streamlit langchain
```

---

# 🤖 Run Ollama

Install Ollama from:
https://ollama.com

Run Llama3 locally:

```bash
ollama run llama3
```

---

# 🧪 Running the Project

## Step 1 — Train Model

```bash
python notebooks/train_model.py
```

---

## Step 2 — Run Backend

```bash
uvicorn backend.main:app --reload
```

---

## Step 3 — Run Frontend

```bash
streamlit run frontend/app.py
```

---

# 📈 Machine Learning Pipeline

```text
Dataset
   ↓
Text Cleaning
   ↓
TF-IDF Vectorization
   ↓
Naive Bayes Training
   ↓
Prediction
```

---

# 🧠 Agent Workflow

```text
User Message
   ↓
Input Agent
   ↓
Spam Detection Agent
   ↓
Threat Analysis Agent
   ↓
Decision Agent
   ↓
Final Output
```

---

# 📌 Example Output

```text
Message:
"Congratulations! You won ₹50,000. Click here now."

Prediction:
SPAM

Confidence:
97%

Threat Type:
Phishing

Explanation:
Contains urgency tactics and suspicious reward claims.
```

---

# 📊 Future Enhancements

* Real-time Email Integration
* WhatsApp Spam Analysis
* Voice Scam Detection
* Adaptive Learning Agent
* Browser Extension
* Cloud Deployment

---

# 👨‍💻 Team Roles

## ML Engineer

* Model Training
* NLP Processing

## Backend Engineer

* FastAPI APIs
* Integration

## Agentic AI Engineer

* LangChain
* LLM Integration

## Frontend Engineer

* Streamlit Dashboard
* UI/UX

---

# 📚 Learning Outcomes

This project helps in learning:

* Machine Learning
* NLP
* Agentic AI
* LangChain
* FastAPI
* Streamlit
* API Integration
* Team Collaboration

---

# 📌 Advantages of the System

✅ Explainable AI
✅ Intelligent Decision Making
✅ Real-Time Analysis
✅ Scalable Architecture
✅ User-Friendly Dashboard

---

# 🏆 Conclusion

The Agentic AI Powered Spam Detection System combines Machine Learning and AI Agents to create an intelligent and explainable spam detection platform.

The project demonstrates:

* AI-powered automation
* Multi-agent reasoning
* NLP processing
* Full-stack AI application development

This system can be extended for:

* cybersecurity,
* fraud detection,
* phishing prevention,
* smart communication filtering.

---

# 📄 License

This project is developed for educational and research purposes.

---

# 🙌 Acknowledgements

* Scikit-learn
* LangChain
* Ollama
* FastAPI
* Streamlit
* Kaggle Dataset Contributors
