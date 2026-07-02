# Databricks notebook source

catalog_name = "olist_ecommerce"

spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog_name}")

schemas = ["raw", "bronze", "silver", "gold", "security"]

for schema in schemas:
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.{schema}")

spark.sql(f"USE CATALOG {catalog_name}")

display(spark.sql(f"SHOW SCHEMAS IN {catalog_name}"))

