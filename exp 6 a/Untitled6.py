#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# DATA PREPARATION & CLEANING
# ============================================================
df = pd.read_csv("C:/Users/DELL/Downloads/startup_funding.csv")

# Clean 'Amount in USD' into numeric format
df['Amount_USD_Clean'] = (
    df['Amount in USD']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.extract(r'(\d+)', expand=False)
)
df['Amount_USD_Clean'] = pd.to_numeric(df['Amount_USD_Clean'], errors='coerce')

# Parse Year from Date column
df['Date_Clean'] = pd.to_datetime(
    df['Date dd/mm/yyyy'].astype(str).str.replace('.', '/', regex=False),
    format='%d/%m/%Y',
    errors='coerce'
)
df['Year'] = df['Date_Clean'].dt.year

# Filter subset for index-based stackplot comparison
df_sample = df.head(100).copy()

# ============================================================
# 1. Line Plot - Year vs Total Funding Amount
# ============================================================
yearly_funding = df.groupby('Year')['Amount_USD_Clean'].sum().dropna()

plt.figure(figsize=(8,5))
plt.plot(yearly_funding.index, yearly_funding.values, alpha=0.8, marker='o')
plt.title("Line Plot: Year vs Total Funding Amount (USD)")
plt.xlabel("Year")
plt.ylabel("Total Funding Amount (USD)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ============================================================
# 2. Box Plot - Funding Amount (Log Scale)
# ============================================================
plt.figure(figsize=(6,5))
plt.boxplot(df["Amount_USD_Clean"].dropna())
plt.title("Funding Amount Box Plot")
plt.ylabel("Amount in USD (Log Scale)")
plt.yscale('log')
plt.tight_layout()
plt.show()

# ============================================================
# 3. Histogram - Funding Year Distribution
# ============================================================
plt.figure(figsize=(8,5))
plt.hist(df["Year"].dropna(), bins=10, edgecolor="black", color="skyblue")
plt.title("Funding Deals Distribution by Year")
plt.xlabel("Year")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ============================================================
# 4. Violin Plot - Funding Amount
# ============================================================
plt.figure(figsize=(6,5))
plt.violinplot(df["Amount_USD_Clean"].dropna())
plt.title("Funding Amount Violin Plot")
plt.ylabel("Amount in USD")
plt.yscale('log')
plt.tight_layout()
plt.show()

# ============================================================
# 5. Line Plot - Funding Amount Trend (by Index)
# ============================================================
plt.figure(figsize=(10,5))
plt.plot(df.index, df["Amount_USD_Clean"], color="red", alpha=0.7)
plt.title("Funding Amount Trend by Record Index")
plt.xlabel("Record Index")
plt.ylabel("Funding Amount (USD)")
plt.yscale('log')
plt.grid(True)
plt.tight_layout()
plt.show()

# ============================================================
# 6. Stack Plot - Sr No & Funding Amount (Sample)
# ============================================================
plt.figure(figsize=(10,5))
plt.stackplot(
    df_sample.index,
    df_sample["Sr No"].fillna(0),
    df_sample["Amount_USD_Clean"].fillna(0) / 1e6,
    labels=["Sr No", "Amount (in Millions USD)"]
)
plt.title("Sr No and Funding Amount (First 100 Records)")
plt.xlabel("Record Index")
plt.ylabel("Values")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()

# ============================================================
# 7. Line Plot - Year by Record Index
# ============================================================
plt.figure(figsize=(12,5))
plt.plot(df.index, df["Year"], color="green", alpha=0.7)
plt.title("Year by Record Index")
plt.xlabel("Record Index")
plt.ylabel("Year")
plt.tight_layout()
plt.show()

# ============================================================
# 8. Pie Chart - Investment Type Distribution
# ============================================================
inv_types = df["InvestmentnType"].str.strip().str.title().value_counts().head(5)

plt.figure(figsize=(7,7))
plt.pie(inv_types,
        labels=inv_types.index,
        autopct="%1.1f%%",
        startangle=90)
plt.title("Top 5 Investment Types Distribution")
plt.tight_layout()
plt.show()

# ============================================================
# 9. Subplots (2x2)
# ============================================================
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# Line Plot
ax[0,0].plot(df.index, df["Amount_USD_Clean"], color="purple", alpha=0.6)
ax[0,0].set_title("Line Plot - Funding Amount")
ax[0,0].set_yscale('log')

# Histogram
ax[0,1].hist(df["Year"].dropna(), bins=8, edgecolor="black", color="orange")
ax[0,1].set_title("Histogram - Year")

# Box Plot
ax[1,0].boxplot(df["Amount_USD_Clean"].dropna())
ax[1,0].set_title("Box Plot - Funding Amount")
ax[1,0].set_yscale('log')

# Scatter Plot
ax[1,1].scatter(df["Sr No"], df["Amount_USD_Clean"], alpha=0.5)
ax[1,1].set_title("Scatter - Sr No vs Funding Amount")
ax[1,1].set_xlabel("Sr No")
ax[1,1].set_ylabel("Funding Amount (USD)")
ax[1,1].set_yscale('log')

plt.tight_layout()
plt.show()

# ============================================================
# 10. Seaborn Scatter Plot
# ============================================================
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="Year", y="Amount_USD_Clean", alpha=0.6)
plt.title("Year vs Funding Amount (Seaborn)")
plt.yscale('log')
plt.tight_layout()
plt.show()


# In[ ]:




