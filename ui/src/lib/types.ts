export interface Item {
  description: string | null;
  quantity: number | null;
  total_price: number | null;
}

export interface Receipt {
  receipt_type: string;
  currency: string | null;
  total: number | null;
  total_tax: number | null;
  tax_details: number | null;
  merchant_address: string | null;
  merchant_name: string | null;
  transaction_date: string;
  transaction_time: string;
  items: Item[];
}
