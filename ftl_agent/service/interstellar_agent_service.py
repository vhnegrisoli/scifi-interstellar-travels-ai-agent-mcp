from agent.agent import InterstellarAgent
from model.chat import ChatRequest, ChatResponse


class AgentValidationError(Exception):
    pass


class AgentInvocationError(Exception):
    pass


class InterstellarAgentService:
    def __init__(self):
        self._agent = InterstellarAgent()

    async def chat(self, request: ChatRequest) -> ChatResponse:
        prompt = ""
        self._validate_input(request)

        if self._is_chat_memory_supported(request):
            prompt = self._build_prompt_with_memory(request)
        else:
            prompt = request.message

        try:
            agent_response = await self._agent.invoke(prompt)
            return agent_response
        except Exception as ex:
            raise AgentInvocationError(f"Error invoking agent: {str(ex)}")

    def _validate_input(self, request: ChatRequest) -> bool:
        if not request.message and not request.messages:
            raise AgentValidationError("Invalid input: either 'message' or 'messages' must be provided.")

    def _is_chat_memory_supported(self, request: ChatRequest) -> bool:
        return bool(not request.message and request.messages)

    def _build_prompt_with_memory(self, request: ChatRequest) -> str:
        prompt = ""

        for message in request.messages:
            prompt += f"{message.role}: {message.content}\n"

        return prompt
