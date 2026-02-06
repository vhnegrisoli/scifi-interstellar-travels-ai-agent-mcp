import os
from strands.models.openai import OpenAIModel
from dotenv import load_dotenv
from model.provider import LLMProvider


load_dotenv()

MAX_TOKENS = 5000
OPENAI_ENDPOINT = "https://api.openai.com/v1"


class AgentModel():

    def __init__(self, provider: LLMProvider = LLMProvider.OPENAI):
        self._key = os.getenv("LLM_KEY", "")
        self._model = os.getenv("LLM_MODEL", "")
        self._base_url = self._get_provider_url(provider)

    def get_model(self, ) -> OpenAIModel:
        return OpenAIModel(
            client_args={
                "api_key": self._key,
                "base_url": self._base_url
            },
            model_id=self._model,
            params={
                "max_completion_tokens": MAX_TOKENS,
            }
        )

    def _get_provider_url(self, provider: LLMProvider) -> str:
        if provider == LLMProvider.OPENAI:
            return OPENAI_ENDPOINT
        elif provider == LLMProvider.AZURE_OPENAI:
            return os.getenv("AZURE_OPENAI_BASE_URL", "")
        else:
            raise ValueError(f"Unsupported provider: {provider}")
