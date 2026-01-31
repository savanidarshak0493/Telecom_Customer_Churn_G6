Clustering Analysis Folder created# Clustering Analysis – Stage 2 (2-2)

## Objective
The objective of this stage is to perform clustering analysis to identify distinct customer segments based on key behavioural and service-related features. This analysis helps in understanding customer patterns and supports future churn prediction and retention strategies.

## Input Data
The clustering analysis uses the processed datasets generated during Stage 2 – Data Preparation.

Files used:
- X_train.csv
- X_test.csv

Only feature datasets were used because clustering is an unsupervised learning technique. Churn labels were not used for training the clustering model.

## Methodology

### Elbow Method
The Elbow Method was applied to determine the optimal number of clusters by analysing the Within-Cluster Sum of Squares (WCSS). The point where the reduction in WCSS begins to slow down was selected as the optimal number of clusters.

### K-Means Clustering
A K-Means clustering model was trained using the optimal number of clusters identified through the Elbow Method. This model groups customers based on similarity in their features.

### Cluster Visualisation
Principal Component Analysis (PCA) was applied to reduce the dimensionality of the dataset and visualise customer clusters in two dimensions for better interpretation.

## Output Files
The following outputs were generated as part of the clustering analysis:

- 01_elbow_method.png  
  Visualisation used to identify the optimal number of clusters.

- 02_kmeans_model.pkl  
  Saved trained K-Means clustering model.

- 03_cluster_visualization.png  
  PCA-based visual representation of customer clusters.

- 04_clustered_dataset.csv  
  Dataset containing cluster labels assigned to each customer.

## Business Insight
The resulting clusters represent distinct customer segments with different usage and behavioural patterns. These insights can be used to design targeted customer retention strategies and support churn prediction in later stages of the project.

## Conclusion
This clustering analysis completes Stage 2 (2-2) deliverables by successfully identifying customer segments and preparing structured outputs for further modelling and analysis.
