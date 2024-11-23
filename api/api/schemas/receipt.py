from datetime import date, time

from pydantic import BaseModel, Field


class Item(BaseModel):
    description: str = Field(alias="Description")
    quantity: int = Field(alias="Quantity")
    total_price: float = Field(alias="TotalPrice")


class Receipt(BaseModel):
    receipt_type: str = Field(alias="Type")
    items: list[Item] = Field(default_factory=list, alias="Items")
    total: float = Field(alias="Total")
    total_tax: float | None = Field(None, alias="TotalTax")
    tax_details: float | None = Field(None, alias="TaxDetails")
    merchant_address: str | None = Field(None, alias="MerchantAddress")
    merchant_name: str = Field(alias="MerchantName")
    transaction_date: date | None = Field(None, alias="TransactionDate")
    transaction_time: time | None = Field(None, alias="TransactionTime")
