# 04_save_processed_data.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import os

# -----------------------------
# 1. Load Dataset
# -----------------------------
file_path = "../../Data_Preparation/Raw_Data/Dataset_ATS_v2.csv"
df = pd.read_csv(file_path)

print("Dataset loaded for saving processed data")
print("-" * 50)

# -----------------------------
# 2. Encode Categorical Variables
# -----------------------------
categorical_cols = ['gender', 'Dependents', 'PhoneService', 'MultipleLines', 
                    'InternetService', 'Contract', 'Churn']

le_dict = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    le_dict[col] = le

# -----------------------------
# 3. Scale Numeric Features
# -----------------------------
numeric_cols = ['tenure', 'MonthlyCharges']
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# -----------------------------
# 4. Split Dataset
# -----------------------------
X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 5. Save Processed Data
# -----------------------------
processed_folder = "../../Data_Preparation/processed_data"

# Create folder if it doesn't exist
os.makedirs(processed_folder, exist_ok=True)

X_train.to_csv(os.path.join(processed_folder, "X_train.csv"), index=False)
X_test.to_csv(os.path.join(processed_folder, "X_test.csv"), index=False)
y_train.to_csv(os.path.join(processed_folder, "y_train.csv"), index=False)
y_test.to_csv(os.path.join(processed_folder, "y_test.csv"), index=False)

print(f"Processed data saved successfully in {processed_folder}")
print("-" * 50)