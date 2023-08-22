from typing import List

import streamlit as st
from streamlit_chat import message

from src.agent import Agent
from src.chat import CHAT_TYPE_SYSTEM, Chat

CHAT_LATEST: str = "latest_chat"


def run_agent():
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


def show_conv(conv_history: List[Chat]):
    """Show conversation history
    Args:
        conv_history (List[Chat]): conversation history
    """
    for i in range(len(conv_history) - 1, -1, -1):
        if conv_history[i].type == CHAT_TYPE_SYSTEM:
            message(conv_history[i].text, key=str(i))
        else:
            message(conv_history[i].text, is_user=True, key=str(i) + "_user")


def main():
    run_agent()


if __name__ == "__main__":
    main()
