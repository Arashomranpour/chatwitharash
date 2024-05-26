import streamlit as st
import google.generativeai as gen
from PIL import Image

# Configure the Google Generative AI API
gen.configure(api_key="AIzaSyDaFygGK9ocbwn1JRNKrB5_4H59dXmd8Dg")
model = gen.GenerativeModel("gemini-pro")

# Initialize the chat history and prompt in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

# Function to convert chat history to text
def convert_chat_history_to_text(chat_history):
    history_text = ""
    for sender, message in chat_history:
        history_text += f"{sender}: {message}\n\n"
    return history_text

# Function to clear chat history and prompt
def clear_chat_history():
    st.session_state.chat_history = []
    st.session_state.prompt = ""

# Display the header
st.header("Chat with Arash")

# Sidebar for user inputs
st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose an option", ["Ask a question", "Ask a question from an image"])

if option == "Ask a question":
    st.session_state.prompt = st.text_input("Ask your question:", value=st.session_state.prompt)

    # If there's a prompt, generate a response and update the chat history
    if st.button("Submit") and st.session_state.prompt:
        with st.chat_message("User"):
            st.session_state.chat_history.append(("User", st.session_state.prompt))
            st.write(st.session_state.prompt)
        
        # Generate a response from the model
        res = model.generate_content(st.session_state.prompt)
        
        with st.chat_message("Arash"):
            st.write(res.text)
            st.session_state.chat_history.append(("Arash", res.text))
        
        # Clear the prompt
        st.session_state.prompt = ""
        
    # Display the chat history
    if st.session_state.chat_history:
        st.divider()
        st.write("History :")
        for sender, message in st.session_state.chat_history:
            with st.chat_message(sender):
                st.write(message)
        
        # Convert chat history to text
        chat_history_text = convert_chat_history_to_text(st.session_state.chat_history)
        
        # Layout for download and clear buttons
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                label="Download Chat History",
                data=chat_history_text,
                file_name="chat_history.txt",
                mime="text/plain"
            )
        
        with col2:
            if st.button("Clear Chat History"):
                clear_chat_history()
                st.experimental_rerun()

elif option == "Ask a question from an image":
    input_prompt = st.text_input("Input prompt:", key="input")
    upload_file = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])

    if upload_file is not None:
        image = Image.open(upload_file)
        st.image(image, use_column_width=True, caption="Uploaded Image")
    
    if st.button("Submit", key="submit_image"):
        if upload_file is not None:
            image_data = Image.open(upload_file)
            model_vision = gen.GenerativeModel("gemini-pro-vision")
            res = model_vision.generate_content([default_input_prompt, image_data, input_prompt])
            st.subheader("The Response:")
            st.write(res.text)
        else:
            st.write("Please upload an image first.")
