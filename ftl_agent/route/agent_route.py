from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status

from model.chat import ChatRequest
from service.interstellar_agent_service import AgentValidationError, InterstellarAgentService


agent_route = APIRouter()
service = InterstellarAgentService()


@agent_route.post("/agent")
async def invoke_agent(request: ChatRequest):
    try:
        response = await service.chat(request)
        return JSONResponse(
            content=response.model_dump(),
            status_code=status.HTTP_200_OK
        )
    except AgentValidationError as ave:
        return JSONResponse(
            content={"error": str(ave)},
            status_code=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
