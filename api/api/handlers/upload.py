from fastapi import UploadFile
from langchain_ollama import ChatOllama

from api.schemas.receipt import Receipt
from api.settings import settings


async def upload(file: UploadFile):
    llm = ChatOllama(
        base_url=settings.OLLAMA_URL,
        model=settings.OLLAMA_MODEL_NAME,
        format="json",
    ).with_structured_output(Receipt)
