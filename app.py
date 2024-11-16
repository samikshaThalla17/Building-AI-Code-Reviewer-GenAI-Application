import google.generativeai as genai
import streamlit as st

# Set up Google Generative AI (GenAI) API key
with open(r"C:\Users\nikhi\Desktop\gemini\key\key.txt","r") as f:
    key = f.read().strip()

# Configure the Generative AI API keys
genai.configure(api_key = "AIzaSyDMLTyTHm434cCiU6wqisAbpNZ2jiz4kd4")

# Title of the app
st.title("GenAI App - AI Code Reviewer")

# Subtitle of the app
st.subheader("Submit your Python code for detailed analysis and receive insightful suggestions and improvements instantly!")

# Input area for Python code
user_prompt = st.text_area("Enter your Python code here:", placeholder="Paste your code here.....", height=150)

# Button to generate review when clicked
if st.button("Generate Review"):
    if user_prompt.strip():
        try:
            # Initialize the model
            model = genai.GenerativeModel("models/gemini-1.5-flash")

            # Start a chat session with the model
            ai_assistant = model.start_chat(history=[])

            # Generate the chat response
            response = ai_assistant.send_message(
                f"Please review the following Python code for errors or improvements:\n\n{user_prompt}\n\nProvide feedback and suggest fixes if necessary."
            )
            
            # Display the subheader in green color
            st.markdown("<h2 style='color: green;'>Corrected Code and Review:</h2>", unsafe_allow_html=True)

            # Display the chat response
            st.write(response.text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter your Python code.")
