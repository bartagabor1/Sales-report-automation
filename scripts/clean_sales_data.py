import pandas as pd
import os

# Define file paths
sales_path = "data/sales.csv"
products_path = "data/products.csv"
customers_path = "data/customers.csv"
output_path = "data/cleaned_sales_data.csv"

# Load CSV files
sales_df = pd.read_csv(sales_path)
products_df = pd.read_csv(products_path)
customers_df = pd.read_csv(customers_path)

# Merge sales with products (on product_id)
merged_df = sales_df.merge(products_df, on="product_id", how="left")

# Merge with customers (on customer_id)
merged_df = merged_df.merge(customers_df, on="customer_id", how="left")

# Check for missing values
missing_values = merged_df.isnull().sum()
print("🔍 Missing values per column:\n", missing_values)

# Drop rows with any missing values (optional - depends on project rules)
merged_df.dropna(inplace=True)

# Check for duplicates
duplicates = merged_df.duplicated().sum()
print(f"🧼 Number of duplicate rows: {duplicates}")

# Drop duplicates (if any)
merged_df.drop_duplicates(inplace=True)

# Export cleaned data
os.makedirs("data", exist_ok=True)
merged_df.to_csv(output_path, index=False)

print(f"✅ Cleaned sales data saved to: {output_path}")
