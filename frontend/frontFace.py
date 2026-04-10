import streamlit as st
import requests

st.title("Welcome to my Youtube Bot")
st.set_page_config(page_title="My First App", layout="wide")

st.write("This is a simple Streamlit app that demonstrates how to create a user interface for a YouTube bot. You can use this app to interact with the bot and perform various actions such as searching for videos, liking videos, and subscribing to channels.")

backend_url = "http://localhost:8000"
st.header("Chat with Videos")
url = st.text_input("Enter YouTube URL")

if st.button("Process Video"):
    res = requests.post(f"{backend_url}/process_video", json={"url": url})
    st.write(res.json())

query = st.text_input("Ask a question")

if st.button("Ask"):
    res = requests.post(f"{backend_url}/chat", json={"query": query})
    st.write(res.json()["answer"])