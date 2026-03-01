# Processed Data

This folder contains cleaned and transformed datasets generated from the raw data.

The data preprocessing steps were carried out using scripts from **`Scripts/data_preparation_script`**, which include:
1. **One-Hot Encoding** for categorical variables such as `InternetService` and `Contract`.
2. **Scaling** for continuous variables like `tenure` and `MonthlyCharges`.

Only scripts inside **`Scripts/data_preparation_script`** are allowed to write files here.

---

## Files Included:
- **X_train.csv**: Processed feature data for training the model.
- **X_test.csv**: Processed feature data for testing the model.
- **y_train.csv**: Target labels for training.
- **y_test.csv**: Target labels for testing.
