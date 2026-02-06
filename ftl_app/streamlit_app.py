import os
import streamlit as st
import requests
from dotenv import load_dotenv


load_dotenv()


AGENT_URL = os.getenv("AGENT_URL", "http://localhost:8000")

st.title("Interstellar Travel Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Digite sua mensagem"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = requests.post(
                f"{AGENT_URL}/api/interstellar/agent",
                json={"messages": st.session_state.messages},
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            content = data.get("content", "Sem resposta")
            st.markdown(content)
            st.session_state.messages.append({"role": "assistant", "content": content})
        except Exception as e:
            error_msg = f"Erro: {str(e)}"
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
