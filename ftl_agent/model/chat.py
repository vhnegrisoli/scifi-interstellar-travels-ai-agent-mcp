from typing import List
from pydantic import BaseModel, Field


class MessageInput(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str | None = None
    messages: List[MessageInput] = Field(default_factory=list)


class TokenUsage(BaseModel):
    input_tokens: int
    output_tokens: int
    total_tokens: int


class ChatResponse(BaseModel):
    role: str
    content: str
    usage: TokenUsage | None = None
