import os
from strands.models.openai import OpenAIModel
from dotenv import load_dotenv


load_dotenv()


class AgentModel():

    def __init__(self):
        self._key = os.getenv("OPENAI_KEY", "")
        self._model = os.getenv("OPENAI_MODEL", "")

    def get_model(self) -> OpenAIModel:
        return OpenAIModel(
            client_args={
                "api_key": self._key,
            },
            model_id=self._model,
            params={
                "max_completion_tokens": 5000,
                #"temperature": 0.7,
            }
        )
