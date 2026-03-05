# Final Report – Telecom Customer Churn Analysis

## 1. Project Overview

This project focuses on analysing telecom customer behaviour to understand customer churn and predict which customers are likely to leave the service.

The project was completed in three stages:

1. Data Preparation
2. Customer Segmentation using K-Means Clustering
3. Predictive Modelling using Artificial Neural Networks (ANN)

The objective is to provide insights that telecom companies can use to reduce customer churn and improve retention strategies.

---

## 2. Customer Segmentation Findings

K-Means clustering was used to group customers based on their behaviour and service usage.

The optimal number of clusters was identified using the elbow method. The clustering analysis helped identify different types of telecom customers, such as:

• Long-term loyal customers  
• New customers with short tenure  
• High-paying customers with premium services  
• Customers with higher likelihood of churn

These clusters allow businesses to better understand customer behaviour patterns.

---

## 3. Churn Prediction using ANN

An Artificial Neural Network (ANN) model was developed to predict whether a customer will churn.

The model uses customer attributes such as:

• Tenure  
• Monthly charges  
• Contract type  
• Internet services  
• Payment method  
• Demographic attributes

The ANN model consists of:

• Input layer  
• Two hidden layers using ReLU activation  
• Output layer using sigmoid activation

The model was trained using the Adam optimizer and binary cross entropy loss function.

The final model achieved an accuracy of approximately **78%**.

Model evaluation included:

• Accuracy graph  
• Loss graph  
• Confusion matrix

---

## 4. Factors Contributing to Customer Churn

Based on the analysis, several factors were identified as contributing to customer churn:

• Customers with **month-to-month contracts** have higher churn rates.  
• Customers with **short tenure** are more likely to leave.  
• Customers with **higher monthly charges** tend to churn more often.  
• Lack of long-term contract commitment increases churn probability.

These patterns indicate that pricing and contract structure play a significant role in customer retention.

---

## 5. Recommendations for Retention Strategies

Based on the findings, telecom companies can implement the following strategies:

• Encourage customers to switch from month-to-month plans to **long-term contracts**.  
• Offer **discounts or loyalty rewards** to new customers during their early tenure.  
• Provide targeted promotions to **high-risk customers identified by the ANN model**.  
• Improve service packages for high-paying customers to increase satisfaction.

These strategies can help telecom companies reduce churn and improve long-term revenue.

---

## 6. Limitations

Although the model performs reasonably well, there are several limitations:

• The dataset size is limited and may not represent all customer behaviours.  
• Class imbalance may affect churn prediction accuracy.  
• The ANN architecture could be further improved using additional tuning.

Future improvements may include:

• Hyperparameter tuning  
• More advanced models such as Gradient Boosting or Deep Neural Networks  
• Additional customer behaviour features.

---

## 7. Conclusion

This project successfully demonstrated how machine learning techniques can be applied to analyse customer churn.

Customer segmentation using clustering and churn prediction using ANN provide valuable insights that telecom companies can use to improve customer retention strategies and make data-driven decisions.