# 01_data_loading_and_validation.py

import pandas as pd

# -----------------------------
# 1. Load Dataset
# -----------------------------
file_path = "../../Data_Preparation/Raw_Data/Dataset_ATS_v2.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully")
print("-" * 50)

# -----------------------------
# 2. Basic Information
# -----------------------------
print("Shape of dataset (rows, columns):")
print(df.shape)
print("-" * 50)

print("Column names:")
print(df.columns.tolist())
print("-" * 50)

# -----------------------------
# 3. Data Types
# -----------------------------
print("Data types:")
print(df.dtypes)
print("-" * 50)

# -----------------------------
# 4. Missing Values Check
# -----------------------------
print("Missing values per column:")
print(df.isnull().sum())
print("-" * 50)

# -----------------------------
# 5. Unique Values per Column
# -----------------------------
print("Unique values per column:")
for col in df.columns:
    print(f"\nColumn: {col}")
    print(df[col].unique())

print("-" * 50)
print("Data validation completed")