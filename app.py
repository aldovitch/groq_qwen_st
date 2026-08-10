from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

llm = ChatGroq(model="qwen/qwen3.6-27b")

st.set_page_config(page_title="Chat Qwen", layout="centered")
st.title("Teste com Qwen (ao invés de DeepSeek)")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("🗑️ Limpar memória"):
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

in_message = st.chat_input("Envie sua dúvida:")
if in_message:
    st.session_state.messages.append({"role": "human", "content": in_message})
    st.chat_message("human").markdown(in_message)

    response = llm.invoke(st.session_state.messages)

    st.session_state.messages.append({"role": "ai", "content": response.content})
    st.chat_message("ai").markdown(response.content)
