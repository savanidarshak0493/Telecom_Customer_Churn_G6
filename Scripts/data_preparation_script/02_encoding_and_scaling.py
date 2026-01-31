# 03_encoding_and_scaling.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# -----------------------------
# 1. Load Preprocessed Dataset
# -----------------------------
file_path = "../../Data_Preparation/Raw_Data/Dataset_ATS_v2.csv"

df = pd.read_csv(file_path)

print("Dataset loaded for encoding and scaling")
print("-" * 50)

# -----------------------------
# 2. Encode Categorical Variables
# -----------------------------
# Columns to encode
categorical_cols = ['gender', 'Dependents', 'PhoneService', 'MultipleLines', 
                    'InternetService', 'Contract', 'Churn']

le_dict = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    le_dict[col] = le  # save encoder for future use

print("Categorical columns encoded successfully")
print("-" * 50)

# -----------------------------
# 3. Scale Numeric Features
# -----------------------------
numeric_cols = ['tenure', 'MonthlyCharges']
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("Numeric features scaled successfully")
print("-" * 50)

# -----------------------------
# 4. Split Dataset
# -----------------------------
X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")
print("-" * 50)

print("Encoding, scaling, and splitting completed")
