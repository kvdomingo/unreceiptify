from io import BytesIO
from typing import IO

from azure.ai.documentintelligence.models import AnalyzeResult
from pillow_heif import register_heif_opener

from api.dependencies import doc_intel_client
from api.schemas import Receipt

register_heif_opener()


async def extract_receipt_details(file: IO[bytes]) -> Receipt:
    with BytesIO(file.read()) as buffer:
        buffer.seek(0)
        poller = await doc_intel_client.begin_analyze_document(
            "prebuilt-receipt",
            analyze_request=buffer,
            content_type="application/octet-stream",
        )
        res: AnalyzeResult = await poller.result()

    return Receipt.model_validate(res.documents[0])
