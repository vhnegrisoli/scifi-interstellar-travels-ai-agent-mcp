import asyncio
from fastmcp import Client, FastMCP

server = FastMCP("TestServer")
client = Client(server)

# HTTP server
client = Client("http://localhost:3000/mcp")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()

        # List available operations
        tools = await client.list_tools()

        for tool in tools:
            print(f"Tool: {tool.model_dump_json()}\n")

        info_function_call = await client.call_tool("get_interstellar_db_info")
        print(f"info_function_call: {info_function_call.content}\n")

        id_function_call = await client.call_tool("find_by_id", {"id": "duna_holtzman_foldspace"})
        print(f"id_function_call: {id_function_call.content}\n")

        type_function_call = await client.call_tool("find_by_type", {"type": "Salto pelo Hiperspaço"})
        print(f"type_function_call: {type_function_call.content}\n")

        work_function_call = await client.call_tool("find_by_work", {"work": "Duna"})
        print(f"work_function_call: {work_function_call.content}\n")

asyncio.run(main())