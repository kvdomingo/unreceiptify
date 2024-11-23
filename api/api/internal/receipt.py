from io import BytesIO
from typing import IO

from azure.ai.documentintelligence.models import (
    AnalyzeResult,
    DocumentField,
    DocumentFieldType,
)
from pillow_heif import register_heif_opener

from api.dependencies import doc_intel_client
from api.schemas.receipt import Receipt

register_heif_opener()


def extract_value(value: DocumentField):
    match value.type:
        case DocumentFieldType.STRING:
            return value.value_string
        case DocumentFieldType.NUMBER:
            return value.value_number
        case DocumentFieldType.ADDRESS:
            return value.content.replace("\n", " ")
        case DocumentFieldType.DATE:
            return value.value_date
        case DocumentFieldType.TIME:
            return value.value_time
        case DocumentFieldType.CURRENCY:
            return value.value_currency.amount
        case _:
            return None


async def analyze_receipt(file: IO[bytes]) -> AnalyzeResult:
    with BytesIO(file.read()) as buffer:
        buffer.seek(0)
        poller = await doc_intel_client.begin_analyze_document(
            "prebuilt-receipt",
            analyze_request=buffer,
            content_type="application/octet-stream",
        )
        return await poller.result()


def extract_details(result: AnalyzeResult) -> dict:
    document = result.documents[0]
    out = {
        "Type": document.doc_type,
        "Items": [],
    }

    if (total := document.fields.get("Total")) is not None:
        out["Total"] = extract_value(total)

    if (total_tax := document.fields.get("TotalTax")) is not None:
        out["TotalTax"] = extract_value(total_tax)

    if (tax_details := document.fields.get("TaxDetails")) is not None:
        if len(tax_details_arr := tax_details.value_array) > 0:
            if (
                tax_amount := tax_details_arr[0].value_object.get("Amount")
            ) is not None:
                out["TaxDetails"] = extract_value(tax_amount)

    for key, value in document.fields.items():
        if key in [
            "MerchantAddress",
            "MerchantName",
            "TransactionDate",
            "TransactionTime",
        ]:
            out[key] = extract_value(value)

        if key == "Items":
            for item in value.value_array:
                out["Items"].append(
                    {
                        k: extract_value(v)
                        for k, v in item.value_object.items()
                        if k in ["Description", "Quantity", "TotalPrice"]
                    }
                )

    return out


async def extract_receipt_details(file: IO[bytes]) -> Receipt:
    res = await analyze_receipt(file)
    deets = extract_details(res)
    return Receipt(**deets)
