from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.agent_engine import AgentOrchestrator
from app.utils.logger import logger

router = APIRouter()
orchestrator = AgentOrchestrator()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        logger.info(f"User Request: {request.message}")
        result = orchestrator.process_request(request.message)
        return {"status": "success", "response": result}
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail="Agent loop failed")