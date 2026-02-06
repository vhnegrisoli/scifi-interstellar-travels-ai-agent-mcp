from enum import Enum


class LLMProvider(str, Enum):
    OPENAI = "OPENAI"
    AZURE_OPENAI = "AZURE_OPENAI"
