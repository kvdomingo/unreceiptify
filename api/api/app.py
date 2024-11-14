from contextlib import asynccontextmanager

from fastapi import FastAPI, UploadFile

from api.dependencies import ollama_client
from api.handlers.upload import upload as upload_handler
from api.settings import settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    await ollama_client.pull(settings.OLLAMA_MODEL_NAME)
    yield


app = FastAPI(
    title="Unreceiptify API",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan,
)


@app.get("/api/health")
async def health():
    return {"status": "ok"}


@app.get("/api/upload")
async def upload(file: UploadFile):
    return upload_handler(file)
