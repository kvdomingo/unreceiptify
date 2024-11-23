from datetime import date, time

from pydantic import (
    AliasPath,
    Field,
    field_validator,
)

from .base import BaseModel


class Item(BaseModel):
    description: str | None = Field(
        None,
        validation_alias=AliasPath(
            "valueObject",
            "Description",
            "valueString",
        ),
    )
    quantity: int | None = Field(
        None,
        validation_alias=AliasPath(
            "valueObject",
            "Quantity",
            "valueNumber",
        ),
    )
    total_price: float | None = Field(
        None,
        validation_alias=AliasPath(
            "valueObject",
            "TotalPrice",
            "valueCurrency",
            "amount",
        ),
    )


class Receipt(BaseModel):
    receipt_type: str = Field(validation_alias=AliasPath("docType"))
    currency: str | None = Field(
        None,
        min_length=3,
        max_length=3,
        validation_alias=AliasPath("fields", "Total", "valueCurrency", "currencyCode"),
    )
    total: float | None = Field(
        None,
        validation_alias=AliasPath(
            "fields",
            "Total",
            "valueCurrency",
            "amount",
        ),
    )
    total_tax: float | None = Field(
        None,
        validation_alias=AliasPath(
            "fields",
            "TotalTax",
            "valueCurrency",
            "amount",
        ),
    )
    tax_details: float | None = Field(
        None,
        validation_alias=AliasPath(
            "fields",
            "TaxDetails",
            "valueArray",
            0,
            "valueObject",
            "Amount",
            "valueCurrency",
            "amount",
        ),
    )
    merchant_address: str | None = Field(
        None, validation_alias=AliasPath("fields", "MerchantAddress", "content")
    )
    merchant_name: str | None = Field(
        None, validation_alias=AliasPath("fields", "MerchantName", "valueString")
    )
    transaction_date: date | None = Field(
        None, validation_alias=AliasPath("fields", "TransactionDate", "valueDate")
    )
    transaction_time: time | None = Field(
        None, validation_alias=AliasPath("fields", "TransactionTime", "valueTime")
    )
    items: list[Item] = Field(
        default_factory=list,
        validation_alias=AliasPath("fields", "Items", "valueArray"),
    )

    @field_validator("merchant_address", mode="after")
    @classmethod
    def flatten_merchant_address(cls, v: str | None):
        if v is not None:
            return v.replace("\n", " ")
        return v
