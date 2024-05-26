
# import streamlit as st
# import google.generativeai as gen
# from PIL import Image

# # Configure the Google Generative AI API
# gen.configure(api_key="AIzaSyDaFygGK9ocbwn1JRNKrB5_4H59dXmd8Dg")
# model = gen.GenerativeModel("gemini-pro")

# # Initialize the chat history in session_state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Display the header
# st.header("Chat with Arash")
# tab_a,tab_b=st.tabs(["Ask","do you have any question from an Image?"])
# # Get user input
# with tab_a:
#     prompt = st.chat_input()

# # If there's a prompt, generate a response and update the chat history
#     if prompt:
#         with st.chat_message("User"):
#             # st.write(prompt)
#             st.session_state.chat_history.append(("User", prompt))
        
#         # Generate a response from the model
#         res = model.generate_content(prompt)
        
#         with st.chat_message("Gemini"):
#             st.write(res.text)
#             st.session_state.chat_history.append(("Gemini", res.text))
    
#     # Display the chat history
#     st.divider()
#     st.write("History :")
#     for sender, message in st.session_state.chat_history:
#         with st.chat_message(sender):
#             st.write(message)
# with tab_b:

#     model = gen.GenerativeModel("gemini-pro-vision")

#     def get_res(myinput, img, prompt):
#         response = model.generate_content([myinput, img, prompt])
#         return response.text

#     def input_img(upload_file):
#         if upload_file is not None:
#             image = Image.open(upload_file)
#             return image
#         else:
#             raise FileNotFoundError("No file uploaded, please check")
    
#     input_e = st.text_input("Input prompt :", key="input")
#     upload_file = st.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])

#     if upload_file is not None:
#         image = input_img(upload_file)
#         st.image(image, use_column_width=True, caption="Uploaded Image")
    
#     submit = st.button("Submit")
    
#     input_prompt = """
#     you are an expert in understanding invoices.
#     we will upload an image as invoice and you will have to answer any question based on the uploaded invoice image
#     """
    
#     if submit:
#         if upload_file is not None:
#             image_data = input_img(upload_file)
#             res = get_res(input_prompt, image_data, input_e)
#             st.subheader("The Response:")



# part 2:


import streamlit as st
import google.generativeai as gen
from PIL import Image

# Configure the Google Generative AI API
gen.configure(api_key="AIzaSyDaFygGK9ocbwn1JRNKrB5_4H59dXmd8Dg")
model = gen.GenerativeModel("gemini-pro")

# Initialize the chat history in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to convert chat history to text
def convert_chat_history_to_text(chat_history):
    history_text = ""
    for sender, message in chat_history:
        history_text += f"{sender}: {message}\n\n"
    return history_text

# Function to clear chat history
def clear_chat_history():
    st.session_state.chat_history = []

# Display the header
st.header("Chat with Arash")

# Sidebar for user inputs
st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose an option", ["Ask a question", "Ask a question from an image"])

if option == "Ask a question":
    prompt = st.sidebar.text_input("Ask your question:")

    # If there's a prompt, generate a response and update the chat history
    if prompt:
        with st.chat_message("User"):
            st.session_state.chat_history.append(("User", prompt))
            st.write(prompt)
        
        # Generate a response from the model
        res = model.generate_content(prompt)
        
        with st.chat_message("Gemini"):
            st.write(res.text)
            st.session_state.chat_history.append(("Gemini", res.text))

elif option == "Ask a question from an image":
    input_prompt = st.sidebar.text_input("Input prompt:", key="input")
    upload_file = st.sidebar.file_uploader("Choose an Image", type=["jpg", "jpeg", "png"])

    if upload_file is not None:
        image = Image.open(upload_file)
        st.image(image, use_column_width=True, caption="Uploaded Image")
    
    submit = st.sidebar.button("Submit")
    
    default_input_prompt = """
    You are an expert in understanding invoices.
    We will upload an image as an invoice, and you will have to answer any questions based on the uploaded invoice image.
    """
    
    if submit:
        if upload_file is not None:
            image_data = Image.open(upload_file)
            model_vision = gen.GenerativeModel("gemini-pro-vision")
            res = model_vision.generate_content([default_input_prompt, image_data, input_prompt])
            st.subheader("The Response:")
            st.write(res.text)
        else:
            st.sidebar.write("Please upload an image first.")

# Display the chat history
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
        st.experimental_rerun()  # Rerun the app to reflect changes


#             st.write(res)
#         else:
#             st.write("Please upload an image first.")
