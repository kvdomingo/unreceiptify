from pathlib import Path
from typing import Literal

from pydantic import AnyHttpUrl, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    PYTHON_ENV: Literal["development", "production"] = "production"

    OLLAMA_URL: AnyHttpUrl
    OLLAMA_MODEL_NAME: str = "llava"
    AZURE_AI_ENDPOINT: AnyHttpUrl
    AZURE_AI_ACCESS_KEY: str

    SYSTEM_PROMPT: str = """
    You are a friendly assistant that digitizes receipts. The user will upload images of receipts
    with various orientations and lighting conditions. Your job is to extract key information
    and return it in JSON format with the following structure:

    {
        summary: string,  // A summary of what you see in the picture
        establishment_name: string,  // Name of the establishment that issued the receipt
        address: string,  // Address of the establishment
        vat_number: string,  // The VAT ID of the establishment
        receipt_date: Date,  // Date only of the receipt in YYYY-MM-DD format
        vat_amount: float,  // VAT amount of the receipt
        amount_paid: float,  // Amount paid by the customer
        change: float,  // Change given to the customer
        total_price: float, // Total price of the receipt
        currency: string  // Currency used in the receipt. Use ISO-4217 (3 letter) currency codes.
        items: {
            description: string,  // Name or description of the item
            quantity: int,  // Quantity of the item
            price: float  // Price of the item
        }[]
    }

    All keys should always be present in the response. If the specific information is not in the receipt,
    return null for that key.
    """

    @computed_field
    @property
    def IN_PRODUCTION(self) -> bool:
        return self.PYTHON_ENV == "production"


settings = Settings()
