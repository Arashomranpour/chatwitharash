<div align="center">

# 💬 Chat with Arash

**A Streamlit chatbot powered by Google Gemini that answers text questions and questions about uploaded images.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-4285F4?logo=googlegemini&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

</div>

---

## ✨ Features

- 📝 **Text chat** - ask a question and get an answer from Gemini.
- 🖼️ **Image Q&A** - upload an image, ask something about it and get an answer based on its content.
- 🗂️ **Session history** - the conversation is kept for the session.
- ⬇️ **Download** the chat history as a text file, or 🧹 clear it with one click.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A [Google AI Studio API key](https://aistudio.google.com/app/apikey)

### Install & run

```bash
git clone https://github.com/Arashomranpour/chatwitharash.git
cd chatwitharash
pip install -r requirements.txt
```

Export your key as `GOOGLE_API_KEY`, then:

```bash
streamlit run g.py
```

## 🧭 Usage

| Mode | Steps |
|---|---|
| Text | Choose **Ask a question** in the sidebar → type your question → **Submit** |
| Image | Choose **Ask a question from an image** → upload an image → type a related question → **Submit** |
| History | **Download Chat History** or **Clear Chat History** |

## 📁 Project Structure

```
.
├── g.py               # Streamlit app
└── requirements.txt
```

## 🛠️ Tech Stack

`Streamlit` · `google-generativeai` · `Pillow`
