from dataclasses import dataclass

CHAT_TYPE_SYSTEM = "システム"
CHAT_TYPE_USER = "ユーザー"


@dataclass
class Chat:
    """Chat dataclass"""

    type: str
    text: str

    @classmethod
    def from_data(cls, type: str, text: str):
        if type not in [CHAT_TYPE_SYSTEM, CHAT_TYPE_USER]:
            raise TypeError("error: type must be CHAT_TYPE_SYSTEM or CHAT_TYPE_USER")
        return cls(type=type, text=text)
