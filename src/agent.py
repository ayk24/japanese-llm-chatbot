from typing import List

from .chat import CHAT_TYPE_SYSTEM, CHAT_TYPE_USER, Chat
from .llm import LLM

CONVERSATION_LIMIT = 128


class Agent:
    def __init__(self) -> None:
        self.conv_history: List[Chat] = []
        self.llm = LLM()

    def run(self, user_input: str) -> List:
        """Run agent
        Args:
            user_input (str): user input
        Returns:
            conv_history (List[Chat]): conversation history
        """
        self.conv_history.append(Chat.from_data(CHAT_TYPE_USER, user_input))
        response = self.llm.generate_response(self.conv_history)
        self.conv_history.append(Chat.from_data(CHAT_TYPE_SYSTEM, response))

        if len(self.conv_history) > CONVERSATION_LIMIT:
            self.conv_history.pop(0)

        return self.conv_history

    def get_conv_history(self) -> List[Chat]:
        """Get conversation history
        Returns:
            conv_history (List[Chat]): conversation history
        """
        return self.conv_history
