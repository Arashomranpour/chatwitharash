
import streamlit as st
import google.generativeai as gen

# Configure the Google Generative AI API
gen.configure(api_key="AIzaSyDaFygGK9ocbwn1JRNKrB5_4H59dXmd8Dg")
model = gen.GenerativeModel("gemini-pro")

# Initialize the chat history in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display the header
st.header("Chat with Gemini")

# Get user input
prompt = st.chat_input()

# If there's a prompt, generate a response and update the chat history
if prompt:
    with st.chat_message("User"):
        # st.write(prompt)
        st.session_state.chat_history.append(("User", prompt))
    
    # Generate a response from the model
    res = model.generate_content(prompt)
    
    with st.chat_message("Gemini"):
        st.write(res.text)
        st.session_state.chat_history.append(("Gemini", res.text))

# Display the chat history
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.write(message)
