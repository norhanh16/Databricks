# Olist E-Commerce Databricks Lakehouse

This project builds an end-to-end Lakehouse on Databricks using the Brazilian Olist E-Commerce dataset.

## Concepts Covered

- Auto Loader ingestion
- Bronze/Silver/Gold Medallion Architecture
- Delta Lake MERGE
- SCD Type 2
- Delta Lake time travel
- Delta Change Data Feed
- Delta Live Tables expectations
- OPTIMIZE and ZORDER
- VACUUM
- Unity Catalog governance
- Row-level security
- Column masking
- Gold KPI analytics using PySpark

## Dataset

Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Main Layers

- Bronze: Raw CSV data as Delta tables
- Silver: Cleaned and validated data
- Gold: Business-ready KPI tables