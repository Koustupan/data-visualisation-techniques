#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. LOAD & CLEAN DATASET
# ============================================================
df = pd.read_csv("C:/Users/DELL/Downloads/startup_funding.csv")

# Clean Amount in USD column
df['Amount_USD_Clean'] = (
    df['Amount in USD']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.extract(r'(\d+)', expand=False)
)
df['Amount_USD_Clean'] = pd.to_numeric(df['Amount_USD_Clean'], errors='coerce')

# Parse Year/Month from Date column
df['Date_Clean'] = pd.to_datetime(
    df['Date dd/mm/yyyy'].astype(str).str.replace('.', '/', regex=False),
    format='%d/%m/%Y',
    errors='coerce'
)
df['Year'] = df['Date_Clean'].dt.year

# Filter for recent complete years for clean plotting
df_trend = df[df['Year'].isin([2016, 2017, 2018, 2019])].copy()

# ============================================================
# 2. PLOT 1: LINE CHART (Funding Deals Over Years)
# ============================================================
yearly_deals = df_trend['Year'].value_counts().sort_index()
years = [str(y) for y in yearly_deals.index]
deal_counts = yearly_deals.values

plt.plot(years, deal_counts, marker='o', color='b')
plt.title("Yearly Startup Funding Deals")
plt.xlabel("Year")
plt.ylabel("Number of Deals")
plt.show()

# ============================================================
# 3. PLOT 2: BAR CHART (Deals by Top Cities)
# ============================================================
top_cities = df['City  Location'].str.strip().str.title().value_counts().head(5)
cities = top_cities.index.tolist()
city_counts = top_cities.values

plt.bar(cities, city_counts, color='skyblue')
plt.title("Top 5 Startup Cities by Number of Deals")
plt.xlabel("City Location")
plt.ylabel("Number of Deals")
plt.show()

# ============================================================
# 4. PLOT 3: PIE CHART (Investment Type Breakdown)
# ============================================================
top_inv_types = df['InvestmentnType'].str.strip().str.title().value_counts().head(4)
investment_types = top_inv_types.index.tolist()
inv_counts = top_inv_types.values

plt.pie(inv_counts, labels=investment_types, autopct='%1.1f%%', startangle=140)
plt.title("Investment Type Distribution")
plt.show()

# ============================================================
# 5. PLOT 4: BOXPLOT (Funding Amount in USD - Outlier Check)
# ============================================================
funding_amounts = df['Amount_USD_Clean'].dropna()

plt.boxplot(funding_amounts)
plt.title("Distribution of Startup Funding Amounts (USD)")
plt.ylabel("Amount in USD")
plt.yscale('log')  # Log scale used due to extreme funding values
plt.show()

# ============================================================
# 6. PLOT 5: MULTI-LINE CHART (Total Amount vs Total Deals)
# ============================================================
yearly_metrics = df_trend.groupby('Year').agg(
    Total_Deals=('Sr No', 'count'),
    Total_Amount_Millions=('Amount_USD_Clean', lambda x: x.sum() / 1e6)
).reset_index()

years_multi = [str(y) for y in yearly_metrics['Year']]
deals = yearly_metrics['Total_Deals']
amounts = yearly_metrics['Total_Amount_Millions']

plt.plot(years_multi, deals, label="Total Deals", marker='o')
plt.plot(years_multi, amounts, label="Total Funding ($ Millions)", marker='s')
plt.title("Startup Funding Trends (Deals vs Amount)")
plt.xlabel("Year")
plt.ylabel("Scale")
plt.legend()
plt.show()


# In[ ]:




