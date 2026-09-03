#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# =====================================================
# 1. LOAD DATASET
# =====================================================
file_path = "C:/Users/DELL/Downloads/startup_funding.csv"
df = pd.read_csv(file_path)

print("="*60)
print("DATASET LOADED SUCCESSFULLY")
print("="*60)
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print()

# =====================================================
# 2. BASIC INFORMATION
# =====================================================
print("\n===== INFO =====")
df.info()

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DESCRIPTIVE STATISTICS =====")
print(df.describe(include='all'))

# =====================================================
# 3. CHECK MISSING VALUES
# =====================================================
print("\n===== TOTAL NULL VALUES =====")
print(df.isnull().sum())

print("\n===== TOTAL NA VALUES =====")
print(df.isna().sum())

print("\n===== TOTAL MISSING VALUES =====")
print(df.isnull().sum().sum())

print("\n===== ANY MISSING VALUES? =====")
print(df.isnull().values.any())

print("\n===== MISSING VALUE PERCENTAGE =====")
missing_percent = (df.isnull().sum() / len(df)) * 100
print(missing_percent[missing_percent > 0].sort_values(ascending=False))

# =====================================================
# 4. HANDLE MISSING VALUES (Multiple Techniques)
# =====================================================
# ----- Method 1: Fill with Constant -----
df_constant = df.fillna("Unknown")
print("\n===== CONSTANT FILL ('Unknown') =====")
print(df_constant.isnull().sum().sum(), "missing values remaining")

# Clean 'Amount in USD' to numeric format for numerical imputation techniques
df_num_prep = df.copy()
df_num_prep['Amount_USD_Clean'] = (
    df_num_prep['Amount in USD']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.extract(r'(\d+)', expand=False)
)
df_num_prep['Amount_USD_Clean'] = pd.to_numeric(df_num_prep['Amount_USD_Clean'], errors='coerce')

# ----- Method 2: Mean (for numerical columns) -----
df_mean = df_num_prep.copy()
num_cols = df_mean.select_dtypes(include=[np.number]).columns
for col in num_cols:
    df_mean[col] = df_mean[col].fillna(df_mean[col].mean())
print("\n===== MEAN FILL (Numeric Columns) =====")
print(df_mean[num_cols].isnull().sum().sum(), "numeric missing values remaining")

# ----- Method 3: Median (for numerical columns) -----
df_median = df_num_prep.copy()
for col in num_cols:
    df_median[col] = df_median[col].fillna(df_median[col].median())
print("\n===== MEDIAN FILL (Numeric Columns) =====")
print(df_median[num_cols].isnull().sum().sum(), "numeric missing values remaining")

# ----- Method 4: Mode (for categorical columns) -----
df_mode = df.copy()
cat_cols = df_mode.select_dtypes(include=['object']).columns
for col in cat_cols:
    if df_mode[col].isnull().sum() > 0:
        df_mode[col] = df_mode[col].fillna(df_mode[col].mode()[0])
print("\n===== MODE FILL (Categorical Columns) =====")
print(df_mode[cat_cols].isnull().sum().sum(), "categorical missing values remaining")

# ----- Method 5: Forward Fill -----
df_ffill = df.ffill()
print("\n===== FORWARD FILL =====")
print(df_ffill.isnull().sum().sum(), "missing values remaining")

# ----- Method 6: Backward Fill -----
df_bfill = df.bfill()
print("\n===== BACKWARD FILL =====")
print(df_bfill.isnull().sum().sum(), "missing values remaining")

# =====================================================
# 5. DROP MISSING VALUES (Multiple Techniques)
# =====================================================
df_drop_rows = df.dropna()
print("\n===== DROP ROWS (any missing) =====")
print("Shape after dropping rows:", df_drop_rows.shape)

df_drop_cols = df.dropna(axis=1)
print("\n===== DROP COLUMNS (any missing) =====")
print("Shape after dropping columns:", df_drop_cols.shape)

df_any = df.dropna(how='any')
print("\n===== DROP how='any' =====")
print("Shape:", df_any.shape)

df_all = df.dropna(how='all')
print("\n===== DROP how='all' =====")
print("Shape:", df_all.shape)

df_thresh = df.dropna(thresh=5)          # keep rows with at least 5 non-null values
print("\n===== DROP thresh=5 =====")
print("Shape:", df_thresh.shape)

# Drop only if specific key startup columns are missing
important_cols = ['Startup Name', 'Industry Vertical', 'City  Location', 'Amount in USD']
important_cols = [col for col in important_cols if col in df.columns]
df_subset = df.dropna(subset=important_cols)
print("\n===== DROP SUBSET (important startup columns) =====")
print("Shape:", df_subset.shape)

# =====================================================
# 6. RECOMMENDED CLEANING PIPELINE (Best for projects)
# =====================================================
df_clean = df.copy()

# 1. Clean 'Amount in USD' into numeric format
df_clean['Amount_USD_Clean'] = (
    df_clean['Amount in USD']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.extract(r'(\d+)', expand=False)
)
df_clean['Amount_USD_Clean'] = pd.to_numeric(df_clean['Amount_USD_Clean'], errors='coerce')

# Separate numerical and categorical columns
num_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df_clean.select_dtypes(include=['object']).columns.tolist()

# Fill numerical with median
for col in num_cols:
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())

# Fill categorical with mode
for col in cat_cols:
    if df_clean[col].isnull().sum() > 0:
        df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

print("\n===== FINAL CLEANED DATASET =====")
print("Shape:", df_clean.shape)
print("Remaining missing values:", df_clean.isnull().sum().sum())
print(df_clean.head())


# In[ ]:




