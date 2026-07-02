# Databricks notebook source

raw_path = "/Volumes/olist_ecommerce/raw/files/olist"

files = dbutils.fs.ls(raw_path)

display(files)

customers_path = f"{raw_path}/olist_customers_dataset.csv"

df_customers = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(customers_path)
)

display(df_customers.limit(10))

print(f"Customer rows: {df_customers.count()}")
expected_files = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv"
]

actual_files = [file.name for file in dbutils.fs.ls(raw_path)]

missing_files = [file for file in expected_files if file not in actual_files]

if missing_files:
    raise Exception(f"Missing files: {missing_files}")
else:
    print("All expected Olist CSV files are available.")
