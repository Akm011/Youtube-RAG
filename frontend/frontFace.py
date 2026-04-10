import streamlit as st

st.title("Welcome to my Youtube Bot")
st.set_page_config(page_title="My First App", layout="wide")

st.write("This is a simple Streamlit app that demonstrates how to create a user interface for a YouTube bot. You can use this app to interact with the bot and perform various actions such as searching for videos, liking videos, and subscribing to channels.")

st.header("Chat with Videos")
search_query = st.text_input("Enter a Youtube URL: ")

if st.button("Submit"):
    if search_query:
        # Call the backend function with the UI input
        # result = backend_processor(search_query)
        print("Processing the input...")
        # Display the response
        print(search_query)
        st.success("Data Sent Successfully!")
        # st.info(result)
    else:
        st.warning("Please enter some text first.")