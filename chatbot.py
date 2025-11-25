import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="BHAVYA'S AI CHATBOT", page_icon="🤖")

client = OpenAI(api_key=st.sidebar.text_input("Enter your OpenAI API Key:", type="password"))

st.title("🤖 BHAVYA'S AI CHATBOT")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    bot_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
