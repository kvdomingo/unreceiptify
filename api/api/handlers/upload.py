import magic
from fastapi import HTTPException, UploadFile, status
from pillow_heif import register_heif_opener

from api.internal.receipt import extract_receipt_details

register_heif_opener()

ACCEPTED_TYPES = [
    "image/jpeg",
    "image/png",
    "image/heic",
    "image/heif",
    "image/bmp",
    "image/tiff",
]


async def upload(file: UploadFile):
    if (magic.from_buffer(file.file.read(4096), mime=True)) not in ACCEPTED_TYPES:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Unsupported file type",
        )

    file.file.seek(0)
    return await extract_receipt_details(file.file)
