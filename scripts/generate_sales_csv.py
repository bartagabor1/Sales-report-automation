import pandas as pd
import random
import os
from datetime import datetime, timedelta

# Generate list of customer IDs (C001 to C100)
customer_ids = [f"C{str(i).zfill(3)}" for i in range(1, 101)]

# Generate list of product IDs (P001 to P060)
product_ids = [f"P{str(i).zfill(3)}" for i in range(1, 61)]

# Product prices (should match with products.csv)
product_prices = {
    "P001": 19.99, "P002": 49.99, "P003": 24.99, "P004": 89.99, "P005": 9.99,
    "P006": 15.99, "P007": 129.99, "P008": 299.99, "P009": 179.99, "P010": 109.99,
    "P011": 39.99, "P012": 22.99, "P013": 29.99, "P014": 44.99, "P015": 59.99,
    "P016": 12.99, "P017": 3.99, "P018": 5.99, "P019": 7.99, "P020": 39.99,
    "P021": 6.99, "P022": 19.99, "P023": 2.99, "P024": 13.99, "P025": 8.99,
    "P026": 5.99, "P027": 18.99, "P028": 79.99, "P029": 14.99, "P030": 149.99,
    "P031": 99.99, "P032": 299.99, "P033": 199.99, "P034": 59.99, "P035": 89.99,
    "P036": 139.99, "P037": 249.99, "P038": 159.99, "P039": 249.99, "P040": 149.99,
    "P041": 14.99, "P042": 29.99, "P043": 7.99, "P044": 4.99, "P045": 3.49,
    "P046": 5.49, "P047": 59.99, "P048": 24.99, "P049": 11.99, "P050": 89.99,
    "P051": 19.99, "P052": 16.99, "P053": 9.49, "P054": 6.49, "P055": 10.99,
    "P056": 119.99, "P057": 129.99, "P058": 29.99, "P059": 79.99, "P060": 59.99
}

# Generate sales transactions
sales_data = []
start_date = datetime(2024, 1, 1)

for i in range(1, 501):  # Generate 500 sales records
    sales_id = f"S{str(i).zfill(4)}"
    customer_id = random.choice(customer_ids)
    product_id = random.choice(product_ids)
    date = start_date + timedelta(days=random.randint(0, 365))
    quantity = random.randint(1, 10)
    unit_price = product_prices[product_id]
    revenue = round(quantity * unit_price, 2)

    sales_data.append([
        sales_id,
        customer_id,
        product_id,
        date.strftime("%Y-%m-%d"),
        quantity,
        unit_price,
        revenue
    ])

# Create DataFrame
sales_df = pd.DataFrame(
    sales_data,
    columns=["sales_id", "customer_id", "product_id", "date", "quantity", "unit_price", "revenue"]
)

# Export to CSV inside the 'data/' folder
sales_df.to_csv("data/sales.csv", index=False)

print("✅ 'sales.csv' file generated successfully in the 'data/' folder.")
