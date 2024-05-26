import streamlit as st
import google.generativeai as gen
from PIL import Image
import pandas as pd

# Configure the Google Generative AI API
gen.configure(api_key="AIzaSyDaFygGK9ocbwn1JRNKrB5_4H59dXmd8Dg")
model = gen.GenerativeModel("gemini-pro")

# Initialize the chat history and prompt in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "prompt" not in st.session_state:
    st.session_state.prompt = ""
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

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
option = st.sidebar.selectbox("Choose an option", ["Ask a question", "Ask a question from an image", "Admin Panel"])

if option == "Ask a question":
    st.session_state.prompt = st.text_input("Ask your question:", value=st.session_state.prompt)

    # If there's a prompt, generate a response and update the chat history
    if st.button("Submit") and st.session_state.prompt:
        with st.chat_message("User"):
            st.session_state.chat_history.append(("User", st.session_state.prompt))
            st.write(st.session_state.prompt)
        
        # Generate a response from the model
        try:
            res = model.generate_content(st.session_state.prompt)
            response_text = res.text if hasattr(res, 'text') else "No response text available."
            
            with st.chat_message("Arash"):
                st.write(response_text)
                st.session_state.chat_history.append(("Arash", response_text))
        except Exception as e:
            st.error(f"Error generating response: {e}")
        
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
            default_input_prompt = """
            You are an expert in understanding invoices.
            We will upload an image as an invoice, and you will have to answer any questions based on the uploaded invoice image.
            """
            try:
                res = model_vision.generate_content([default_input_prompt, image_data, input_prompt])
                response_text = res.text if hasattr(res, 'text') else "No response text available."
                st.subheader("The Response:")
                st.write(response_text)
            except Exception as e:
                st.error(f"Error generating response: {e}")
        else:
            st.write("Please upload an image first.")

elif option == "Admin Panel":
    if not st.session_state.admin_logged_in:
        st.subheader("Admin Login")
        password = st.text_input("Enter password:", type="password")
        
        if st.button("Login"):
            if password == "7815":
                st.session_state.admin_logged_in = True
                st.experimental_rerun()
            else:
                st.error("Wrong password. Do not try to login if you are not admin.")
    else:
        st.subheader("Admin Panel")
        
        # Example: Load user data from a CSV file (replace with your data source)
        user_data = pd.read_csv("user_data.csv")  # Replace with your data source
        
        st.write("User Questions:")
        st.dataframe(user_data)

        # Allow admin to view individual user's chat history
        user_id = st.selectbox("Select User ID", user_data["user_id"].unique())
        user_chat_history = user_data[user_data["user_id"] == user_id]["chat_history"]
        
        st.write(f"Chat History for User {user_id}:")
        st.write(user_chat_history.values[0])
