from io import BytesIO
from typing import IO

from fastapi import HTTPException, status
from pillow_heif import register_heif_opener

from api.dependencies import doc_intel_client
from api.schemas import Receipt

register_heif_opener()


async def extract_receipt_details(file: IO[bytes]) -> Receipt:
    with BytesIO(file.read()) as buffer:
        buffer.seek(0)
        poller = await doc_intel_client.begin_analyze_document(
            "prebuilt-receipt",
            buffer,
            content_type="application/octet-stream",
        )
        res = await poller.result()

    if res.documents is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="No results generated from the receipt",
        )

    return Receipt.model_validate(res.documents[0])
