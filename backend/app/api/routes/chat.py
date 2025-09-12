from fastapi import APIRouter
from backend.app.schemas.chat import MessageRequest, MessageResponse
from backend.app.services.chatbot_service import ChatbotLogic
from backend.app.db.neo4j import Neo4jHandler
from backend.app.services.openai_service import OpenAIHandler
from backend.app.core.config import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

router = APIRouter()

_neo4j_h = Neo4jHandler(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)
_openai_h = OpenAIHandler()
_chatbot = ChatbotLogic(_neo4j_h, _openai_h)

@router.post("/chat", response_model=MessageResponse)
async def chat_endpoint(req: MessageRequest) -> MessageResponse:
    reply = _chatbot.chat(req.message)
    return MessageResponse(reply=reply)
