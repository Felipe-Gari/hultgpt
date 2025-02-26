import streamlit as st
from openai import OpenAI

st.title("HultGPT")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Ask me anything..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Store user message in session state
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call OpenAI API to get a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )

    # Get assistant response text
    assistant_response = response.choices[0].message.content

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    
    # Store assistant response in session state
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})