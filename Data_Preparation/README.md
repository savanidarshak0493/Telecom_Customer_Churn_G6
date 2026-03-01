# Data Preparation

This module handles **data cleaning, preprocessing**, and **transformation** to prepare the dataset for analysis and clustering.

### Preprocessing Steps:
1. **Handling Missing Values**: Any missing data points were either imputed or removed to ensure the dataset was clean and ready for analysis.
2. **Categorical Encoding**: **One-Hot Encoding** was applied to nominal categorical variables such as `InternetService` and `Contract` to avoid introducing artificial ordinal relationships that could bias the clustering process.
3. **Scaling**: Continuous numerical features such as `tenure` and `MonthlyCharges` were scaled using **StandardScaler** to ensure that all features contribute equally during the clustering process (important for K-Means, which relies on Euclidean distance).
4. **Data Splitting**: The dataset was split into **training** and **testing** sets using an 80/20 ratio to prepare for any future predictive modeling.

### Input: 
- **Raw_Data** (Original dataset `Dataset_ATS_v2.csv`)

### Output:
- **Processed Data** (Cleaned and transformed datasets, including `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`)

The preprocessing scripts are located in the **`Scripts/data_preparation_script`** directory.
