import os
from typing import List

import ctranslate2
import gdown
from transformers import AutoTokenizer

from .chat import Chat

GOOGLE_DRIVE_URL = "https://drive.google.com/drive/folders/1Rw0hQYBOb7HrouSi_9axVyy8MbI76UG0?usp=sharing"
MODEL_PATH = "models/japanese-large-lm-3.6b-instruction-sft/"


class LLM:
    def __init__(self) -> None:
        if not os.path.exists(MODEL_PATH):
            os.makedirs(MODEL_PATH)
            gdown.download_folder(GOOGLE_DRIVE_URL, output="models/")
        self.generator = ctranslate2.Generator(MODEL_PATH)
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, use_fast=False)

    def generate_response(self, chat_history: List[Chat]) -> str:
        """Generate response from chat history
        Args:
            chat_history (List[Chat]): chat history
        Returns:
            response (str)
        """
        prompt = self.create_prompt(chat_history)
        print(f"prompt: {prompt}")

        tokens = self.tokenizer.convert_ids_to_tokens(
            self.tokenizer.encode(prompt, add_special_tokens=False)
        )

        outputs = self.generator.generate_batch(
            [tokens],
            max_length=256,
            sampling_topk=10,
            sampling_temperature=0.1,
            repetition_penalty=1.1,
            include_prompt_in_result=False,
            cache_static_prompt=True,
            return_scores=True,
        )

        text = self.tokenizer.decode(outputs[0].sequences_ids[0])
        return text

    def create_prompt(self, chat_history: List[Chat]) -> str:
        """Create prompt from chat history
        Args:
            chat_history (List[Chat]): chat history
        Returns:
            prompt (str)
        """
        messages = []
        for chat in chat_history:
            messages.append(f"{chat.type}: {chat.text}")

        prompt = "\n".join(messages)
        prompt = prompt + "\nシステム: "
        return prompt
