export interface Item {
  description: string | null;
  quantity: number | null;
  totalPrice: number | null;
}

export interface Receipt {
  receiptType: string;
  currency: string | null;
  total: number | null;
  totalTax: number | null;
  taxDetails: number | null;
  merchantAddress: string | null;
  merchantName: string | null;
  transactionDate: string;
  transactionTime: string;
  items: Item[];
}
