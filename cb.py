from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=st.secrets["google_api_key"])  ## configuring the api key

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-2.5-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app
st.set_page_config(page_title="Q&A With AI-Expert")

st.header("AI-Expert for all freshers and college students!")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Hi!, I am AI-Expert, your expert helper, how can i help you today?",key="input")
submit=st.button("Ask You're Question!")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("You're Answer:- ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("AI-Expert", chunk.text))
st.subheader("Chat History")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
