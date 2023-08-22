import asyncio
import os
from typing import List

import gdown
import streamlit as st
from streamlit_chat import message

from src.agent import Agent
from src.chat import CHAT_TYPE_SYSTEM, Chat

GOOGLE_DRIVE_URL = "https://drive.google.com/drive/folders/1Rw0hQYBOb7HrouSi_9axVyy8MbI76UG0?usp=sharing"
MODEL_PATH = "models/japanese-large-lm-3.6b-instruction-sft/"
CHAT_LATEST = "latest_chat"


def download_model() -> None:
    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_PATH)
        gdown.download_folder(GOOGLE_DRIVE_URL, output="models/")


def run_agent() -> None:
    """Run chatbot agent"""
    st.title("Chatbot (demo)")
    if "agent" not in st.session_state:
        st.session_state["agent"]: Agent = Agent()

    if CHAT_LATEST not in st.session_state:
        st.session_state[CHAT_LATEST] = "initialize"

    with st.form("chat_form"):
        user_input = st.text_area("質問を入力してください", "", key="input")
        submitted = st.form_submit_button("送信")
        if submitted and st.session_state[CHAT_LATEST] != user_input:
            st.session_state[CHAT_LATEST] = user_input
            st.session_state["agent"].run(user_input)

        conv_history = st.session_state["agent"].get_conv_history()
        show_conv(conv_history)


def show_conv(conv_history: List[Chat]) -> None:
    """Show conversation history
    Args:
        conv_history (List[Chat]): conversation history
    """
    for i in range(len(conv_history) - 1, -1, -1):
        if conv_history[i].type == CHAT_TYPE_SYSTEM:
            message(conv_history[i].text, key=str(i))
        else:
            message(conv_history[i].text, is_user=True, key=str(i) + "_user")


def main() -> None:
    download_model()
    run_agent()


if __name__ == "__main__":
    main()
