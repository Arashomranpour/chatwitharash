# Chat with Arash - Streamlit Application

This is a Streamlit-based chatbot application that leverages Google’s Generative AI API to generate responses based on user queries or questions derived from uploaded images. The app provides two main interaction modes: 
1. Text-based question answering.
2. Image-based question answering.
## Usage
  Text-Based Interaction
  Select “Ask a question” in the sidebar.
  Enter your question and press "Submit".
  View the bot’s response below.
  Image-Based Interaction
  Select “Ask a question from an image” in the sidebar.
  Upload an image and enter a related question.
  Press "Submit" to receive a response based on the image content.
  Chat History Management
  Download: Use the “Download Chat History” button to download your conversation.
  Clear: Use the “Clear Chat History” button to clear the session’s chat history.

## Features

- **Text-Based Chat Mode**: Users can type a question, and the chatbot generates a response. The chat history is displayed and can be downloaded as a text file.
- **Image-Based Question Answering Mode**: Users can upload an image and type a related question, allowing the bot to generate a response based on the image content.
- **Session Management**: Chat history is maintained in the session and can be cleared or downloaded.

## Setup and Configuration

### Prerequisites
- **Python 3.x** 
- **Streamlit**
- **Google Generative AI SDK** (`google.generativeai`)
- **PIL** (Pillow for handling images)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Chat-with-Arash.git
    cd Chat-with-Arash
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the **Google Generative AI API**:
    - Replace `YOUR_API_KEY` in `gen.configure(api_key="YOUR_API_KEY")` with your actual API key.

### Running the Application
To start the Streamlit app, run:
```bash
streamlit run app.py
