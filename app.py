import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key

api_key = st.secrets["TOGETHER_API_KEY"]


# Together AI client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.together.xyz/v1"
)

# Streamlit UI settings
st.set_page_config(page_title="⚡AI-Chatbot", page_icon="🤖", layout="wide")

st.markdown(
    """
    <style>
    .stChatMessage { font-size: 18px; }
    .main { background-color: #f5f7fa; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("💬 AI Chatbot ")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly AI assistant."}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Chat input box
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Together AI
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="meta-llama/Llama-3-8b-chat-hf",
                messages=st.session_state.messages,
                temperature=0.7
            )
            bot_reply = response.choices[0].message.content
            st.markdown(bot_reply)

    # Save bot reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

