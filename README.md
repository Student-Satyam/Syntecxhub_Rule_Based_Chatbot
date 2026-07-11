# Syntecxhub_Rule_Based_Chatbot# 🤖 SyntecxHub - Simple Rule-Based Chatbot

## 📌 Project Overview

This project is a **Simple Rule-Based Chatbot** developed as part of the **SyntecxHub Internship**.

The chatbot combines **rule-based intent matching** with **Mistral AI** using **LangChain**. It responds to greetings, help requests, small talk, and predefined domain questions. If no predefined rule matches the user's input, it uses the Mistral AI model to generate a response.

---

## ✨ Features

* Rule-based intent matching
* Greeting responses
* Help responses
* Small talk support
* Knowledge base for domain-related questions
* AI-powered responses using Mistral AI
* Interactive console-based chat
* Conversation history logging
* Clean and beginner-friendly Python code

---

## 🛠️ Technologies Used

* Python
* LangChain
* Mistral AI API
* python-dotenv

---

## 📂 Project Structure

```text
Syntecxhub_Simple_Rule_Based_Chatbot/
│
├── app.py
├── intents.py
├── knowledge.py
├── history.txt
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/Syntecxhub_Simple_Rule_Based_Chatbot.git
```

2. Move into the project folder

```bash
cd Syntecxhub_Simple_Rule_Based_Chatbot
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file in the project folder and add your Mistral API key:

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💬 Example Conversation

```text
You: Hi
Bot: Hello! How can I help you today?

You: What is Python?
Bot: Python is a high-level programming language.

You: What is Generative AI?
Bot: (Response generated using Mistral AI)

You: Bye
Bot: Goodbye! Have a great day.
```

---

## 📜 Project Requirements Covered

* ✅ Conversational chatbot
* ✅ Rule-based intent matching
* ✅ Greeting intent
* ✅ Help intent
* ✅ Small talk
* ✅ Knowledge base
* ✅ Interactive console
* ✅ Conversation history logging
* ✅ Mistral AI integration using LangChain

---


---

## 👨‍💻 Author

**Satyam Singh**

SyntecxHub Internship Project

