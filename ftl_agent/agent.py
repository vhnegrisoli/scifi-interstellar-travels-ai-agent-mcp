from mcp.client.streamable_http import streamable_http_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
from model import AgentModel


def create_streamable_http_transport():
    return streamable_http_client("http://localhost:3000/mcp/")


streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

with streamable_http_mcp_client:
    tools = streamable_http_mcp_client.list_tools_sync()
    model = AgentModel().get_model()

    for tool in tools:
        print(f"Tool: {tool.tool_name}\n")
        print(f"Spec: {tool.tool_spec}\n")

    agent = Agent(
        model=model,
        tools=tools
    )

    response = agent(
        system_prompt="""
        Você é um assistente de uma base de dados de viagens interestelares.
        Você deve acessar as informações do banco de dados para compreender as opções existentes, e posteriormente,
        quando necessário, sugerir a melhor opção de viagem interestelar para o usuário final com base na base de dados.
        Sempre busque compreender a estrutura e o schema do banco de dados antes de utilizar qualquer outra tool.
        """,
        prompt="Qual obra mais utiliza dobra espacial?"
    )
