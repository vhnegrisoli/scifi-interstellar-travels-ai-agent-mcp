import os
from typing import List
from fastmcp import FastMCP
from dotenv import load_dotenv
import requests


load_dotenv()


INTERSTELLAR_API_BASE_URL = os.getenv(
    "INTERSTELLAR_API_BASE_URL",
    "http://localhost:8000/api/interstellar"
)
HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", 3000))


mcp = FastMCP("Interstellar Travel MCP Server")


def fetch_interstellar_api(
        endpoint: str,
        param: str | None = None
) -> dict:
    url = _build_url(endpoint, param)
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        code = response.status_code
        content = response.text
        return {
            "status_code": code,
            "details": content
        }


def _build_url(endpoint: str, param: str) -> str:
    url = f"{INTERSTELLAR_API_BASE_URL}/{endpoint}"
    if param:
        url += f"/{param}"
    return url


@mcp.tool(
    description="""
    This tool is very important to understand the database structure and content before querying it.
    Always use this tool first to get acquainted with the database.
    To use the other tools, you need to know the DB identifiers (id), types and works related to the interstellar travels, which are all provided by this tool.
    Example of id: 'foundation_hyperspace_jump'
    Example of type: 'Warp Drive'
    Example of work: 'Duna'
    """
)
def get_db_schema() -> dict[str, List[str]]:
    info = fetch_interstellar_api(endpoint="info")
    return info


@mcp.tool(
    description="Find a specific interstellar travel by its unique identifier."
)
def find_by_id(id: str) -> dict[str, str]:
    interstellar_travel = fetch_interstellar_api(
        endpoint="id",
        param=id
    )
    return interstellar_travel


@mcp.tool(
    description="Find interstellar travels by their type, such as 'hyperspace', 'warp drive', etc."
)
def find_by_type(type: str) -> list[dict[str, str]]:
    interstellar_travels = fetch_interstellar_api(
        endpoint="type",
        param=type
    )
    print(interstellar_travels)
    return interstellar_travels


@mcp.tool(
    description="Find interstellar travels by their related work, such as 'Star Wars', 'Dune', 'Foundation', etc"
)
def find_by_work(work: str) -> list[dict[str, str]]:
    interstellar_travels = fetch_interstellar_api(
        endpoint="work",
        param=work
    )
    return interstellar_travels


if __name__ == "__main__":
    print("Starting MCP server with streamable-http transport...")

    mcp.run(
        transport="streamable-http",
        host=HOST,
        port=PORT
    )
