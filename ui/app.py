import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from agent.agent import executor

# Page config
st.set_page_config(page_title="AutoTask Agent", page_icon="🤖")

st.title("🤖 AutoTask Agent")
st.write("Your AI productivity assistant (Emails • Calendar • Notion)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box
user_input = st.chat_input("Ask your assistant...")

if user_input:

    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call your agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking... "):

            response = executor.invoke({"input": user_input})
            output = response["output"]

            st.markdown(output)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": output})