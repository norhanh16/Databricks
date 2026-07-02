# Databricks notebook source

catalog_name = "olist_ecommerce"
schema_name = "raw"
volume_name = "files"

spark.sql(f"""
CREATE VOLUME IF NOT EXISTS {catalog_name}.{schema_name}.{volume_name}
""")

display(spark.sql(f"SHOW VOLUMES IN {catalog_name}.{schema_name}"))

