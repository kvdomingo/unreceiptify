from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import APIRouter, FastAPI, File, UploadFile
from pillow_heif import register_heif_opener

from api.handlers.upload import upload as upload_handler


@asynccontextmanager
async def lifespan(_: FastAPI):
    register_heif_opener()
    yield


app = FastAPI(
    title="Unreceiptify API",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan,
)

api = APIRouter(prefix="/api")


@api.get("/health", tags=["core"])
async def health():
    return {"status": "ok"}


@api.post("/upload", tags=["receipt"])
async def upload(
    file: Annotated[
        UploadFile,
        File(
            description="Image of receipt. Supported types: jpeg, png, heic, heif, bmp, tiff"
        ),
    ],
):
    return await upload_handler(file)


app.include_router(api)
