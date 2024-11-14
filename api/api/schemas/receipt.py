from datetime import date

from pydantic import BaseModel, Field


class Item(BaseModel):
    description: str | None = Field(
        None, description="Name or description of the item."
    )
    quantity: int | None = Field(None, description="Quantity of the item.")
    price: float | None = Field(None, description="Price of the item.")


class Receipt(BaseModel):
    summary: str | None = Field(None, description="Summary of what's in the picture.")
    establishment_name: str | None = Field(
        None, description="Name of the establishment that issued the receipt."
    )
    address: str | None = Field(None, description="Address of the establishment.")
    vat_number: str | None = Field(
        None, description="The VAT number of the establishment."
    )
    receipt_date: date | None = Field(None, description="Date of the receipt.")
    items: list[Item] = Field(None, description="List of items in the receipt.")
    vat_amount: float | None = Field(None, description="VAT of the receipt.")
    amount_paid: float | None = Field(None, description="Amount paid by the customer.")
    change: float | None = Field(None, description="Change given to the customer.")
    total_price: float | None = Field(None, description="Total price of the receipt.")
    currency: str | None = Field(None, description="Currency used in the receipt.")
