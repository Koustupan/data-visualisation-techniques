#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# ============================================================
# 1. LOAD & READ DATASET
# ============================================================
df = pd.read_csv("C:/Users/DELL/Downloads/startup_funding.csv")

print("===== FULL DATA =====")
print(df)

print("\n===== HEAD (First 5 Rows) =====")
print(df.head())

print("\n===== INFO =====")
print(df.info())

print("\n===== DESCRIBE (Summary Statistics) =====")
print(df.describe())

# ============================================================
# 2. BASIC INFO
# ============================================================
print("\n===== SHAPE =====")
print(df.shape)

print("\n===== DATA TYPES =====")
print(df.dtypes)

# ============================================================
# 3. FILTER COLUMNS
# ============================================================
print("\n===== FILTER COLUMNS (Startup Name, Industry Vertical, City Location) =====")
print(df[["Startup Name", "Industry Vertical", "City  Location"]])

print("\n===== FILTER COLUMNS (Investors Name, InvestmentnType, Amount in USD) =====")
print(df[["Investors Name", "InvestmentnType", "Amount in USD"]])

# ============================================================
# 4. FILTER ROWS
# ============================================================
# Clean 'Amount in USD' temporarily for numeric row filtering
df['Amount_USD_Clean'] = (
    df['Amount in USD']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.extract(r'(\d+)', expand=False)
)
df['Amount_USD_Clean'] = pd.to_numeric(df['Amount_USD_Clean'], errors='coerce')

print("\n===== City Location = Bengaluru =====")
print(df[df["City  Location"] == "Bengaluru"])

print("\n===== Industry Vertical = Consumer Internet =====")
print(df[df["Industry Vertical"] == "Consumer Internet"])

print("\n===== Investment Type = Seed Funding =====")
print(df[df["InvestmentnType"] == "Seed Funding"])

print("\n===== Funding Amount > $10,000,000 =====")
print(df[df["Amount_USD_Clean"] > 10000000])

# Multiple Conditions
print("\n===== City Location = Bengaluru AND Industry Vertical = Consumer Internet =====")
print(df[(df["City  Location"] == "Bengaluru") & (df["Industry Vertical"] == "Consumer Internet")])

print("\n===== Funding Amount > $5,000,000 AND Investment Type = Private Equity =====")
print(df[(df["Amount_USD_Clean"] > 5000000) & (df["InvestmentnType"] == "Private Equity")])


# In[ ]:




