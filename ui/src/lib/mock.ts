import type { Receipt } from "@/types";
import { format, parse } from "date-fns";

export const MOCK_RESPONSE: Receipt = {
  merchantName: "Permacura",
  merchantAddress: "1 Earth Avenue, Super Earth",
  receiptType: "receipt.retailMeal",
  transactionDate: "2024-10-27",
  transactionTime: "10:25:00",
  currency: "SES",
  total: 420.69,
  totalTax: 0.69,
  taxDetails: 0.69,
  items: [
    {
      description: "Stims",
      quantity: 4,
      totalPrice: 420.69,
    },
  ],
};

export const MOCK_DATA: Record<string, string | number | null> = {
  "Merchant Name": MOCK_RESPONSE.merchantName,
  "Merchant Address": MOCK_RESPONSE.merchantAddress,
  "Receipt Type": MOCK_RESPONSE.receiptType,
  "Transaction Date": MOCK_RESPONSE.transactionDate,
  "Transaction Time":
    MOCK_RESPONSE.transactionDate && MOCK_RESPONSE.transactionTime
      ? format(
          parse(MOCK_RESPONSE.transactionTime, "hh:mm:ss", MOCK_RESPONSE.transactionDate),
          "h:mm a",
        )
      : null,
  "Currency": MOCK_RESPONSE.currency,
  "Total": MOCK_RESPONSE.total,
  "Tax": MOCK_RESPONSE.totalTax,
};
