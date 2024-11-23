from typing import Annotated

from fastapi import FastAPI, File, UploadFile

from api.handlers.upload import upload as upload_handler

app = FastAPI(
    title="Unreceiptify API",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)


@app.get("/api/health")
async def health():
    return {"status": "ok"}


@app.post("/api/upload")
async def upload(
    file: Annotated[
        UploadFile,
        File(
            description="Image of receipt. Supported types: jpeg, png, heic, heif, bmp, tiff"
        ),
    ],
):
    return await upload_handler(file)
