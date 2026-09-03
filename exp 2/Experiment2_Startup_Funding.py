#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3
import os

print("="*60)
print("EXPERIMENT 2 - DATA LOADING & EXPORTING")
print("="*60)

# -------------------------------------------------
# 1. READ CSV
# -------------------------------------------------
file_path = "C:/Users/DELL/Downloads/startup_funding.csv"

print("\n1. Reading CSV file...")
df = pd.read_csv(file_path)
print("CSV Loaded Successfully!")
print("Shape:", df.shape)

print("\n===== HEAD =====")
print(df.head())

print("\n===== INFO =====")
df.info()

print("\n===== DESCRIBE =====")
print(df.describe())

# -------------------------------------------------
# 2. CONVERT TO EXCEL & READ EXCEL
# -------------------------------------------------
print("\n" + "="*60)
print("2. Converting CSV to Excel and reading it...")
excel_path = "C:/Users/DELL/Downloads/startup_funding.xlsx"
df.to_excel(excel_path, index=False)
print("Excel file created successfully!")

df_excel = pd.read_excel(excel_path)
print("Excel Loaded Successfully!")
print(df_excel.head())

# -------------------------------------------------
# 3. READ FROM SQLITE (In-memory)
# -------------------------------------------------
print("\n" + "="*60)
print("3. Reading data from SQLite database...")
conn = sqlite3.connect(":memory:")
df.to_sql("startup_table", conn, if_exists="replace", index=False)

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in Database:")
print(tables)

table_name = tables.iloc[0, 0]
df_sql = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
print("\n===== HEAD from SQL =====")
print(df_sql.head())

print("\n===== INFO from SQL =====")
df_sql.info()
conn.close()

# -------------------------------------------------
# 4. EXPORT TO CSV
# -------------------------------------------------
print("\n" + "="*60)
print("4. Exporting to CSV...")
df.to_csv("startup_funding_export.csv", index=False)
print("CSV exported successfully! → startup_funding_export.csv")

# -------------------------------------------------
# 5. EXPORT TO EXCEL
# -------------------------------------------------
print("\n5. Exporting to Excel...")
df.to_excel("startup_funding_export.xlsx", index=False)
print("Excel exported successfully! → startup_funding_export.xlsx")

# -------------------------------------------------
# 6. EXPORT TO SQLITE DATABASE
# -------------------------------------------------
print("\n6. Exporting to SQLite database...")
conn = sqlite3.connect("startup_funding.db")
df.to_sql("startup_records", conn, if_exists="replace", index=False)
print("Data exported successfully to SQLite database! → startup_funding.db")
conn.close()

print("\n" + "="*60)
print("ALL STEPS COMPLETED SUCCESSFULLY!")
print("="*60)


# In[ ]:




