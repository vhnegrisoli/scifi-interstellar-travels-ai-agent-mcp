import os
from mcp.client.streamable_http import streamable_http_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
from agent.llm_model import AgentModel
from model.chat import ChatResponse, TokenUsage
from agent.prompts import AGENT_PROMPT


class InterstellarAgent:

    def __init__(self):
        self._mcp_server_url = os.getenv("MCP_SERVER_URL", "http://localhost:3000/mcp/")

    def _connect_to_mcp(self) -> MCPClient:
        return streamable_http_client(self._mcp_server_url)

    async def invoke(self, prompt: str) -> ChatResponse:
        mcp_client = MCPClient(lambda: self._connect_to_mcp())

        with mcp_client:
            tools = mcp_client.list_tools_sync()
            model = AgentModel().get_model()

            agent = Agent(
                model=model,
                tools=tools,
                system_prompt=AGENT_PROMPT
            )

            response = await agent.invoke_async(
                prompt=prompt
            )

            usage = response.metrics.accumulated_usage
            message = response.message

            return ChatResponse(
                role=message.get("role", "assistant"),
                content=message.get("content", [])[0].get("text", ""),
                usage=TokenUsage(
                    input_tokens=usage.get("inputTokens", 0),
                    output_tokens=usage.get("outputTokens", 0),
                    total_tokens=usage.get("totalTokens", 0)
                )
            )
