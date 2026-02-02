# Clustering Analysis – Stage 2 (2-2)

## Project: Telecom Customer Churn Analysis

## 1. Overview
This stage focuses on performing **clustering analysis** to identify distinct customer segments within the telecom dataset.  
Clustering is an **unsupervised machine learning technique** that groups customers based on similarity in their usage and service-related features.

All clustering deliverables are stored in the **Clustering_Analysis** folder as required by the assessment instructions.

---

## 2. Clustering Analysis Deliverables

The following files were created as part of Stage 2 (2-2):

- **01_elbow_method.png** – Elbow Method graph used to determine the optimal number of clusters  
- **02_kmeans_model.pkl** – Trained K-Means clustering model  
- **03_cluster_visualization.png** – Visual representation of customer clusters  
- **04_clustered_dataset.csv** – Dataset containing assigned cluster labels  

---

## 3. Optimal Number of Clusters

### 3.1 What is the Optimal Number of Clusters?
The **optimal number of clusters** refers to the value of *K* that best balances:
- Minimising variation within each cluster
- Avoiding unnecessary complexity from too many clusters

Selecting the correct number of clusters ensures the results are **meaningful, interpretable, and useful** for business analysis.

---

### 3.2 Elbow Method
The **Elbow Method** was used to determine the optimal number of clusters.

This method works by:
1. Training K-Means models with different values of *K*
2. Calculating the **Within-Cluster Sum of Squares (WCSS)** for each value
3. Plotting WCSS against the number of clusters

The optimal number of clusters is identified at the point where the curve begins to flatten, forming an “elbow”.

**Figure 1 below shows the Elbow Method result used in this analysis.**

![Elbow Method](01_elbow_method.png)

Based on the graph, the elbow point indicates the most suitable number of clusters for the dataset.

---

## 4. K-Means Clustering Model

Using the optimal number of clusters identified from the Elbow Method, a **K-Means clustering model** was trained on the processed telecom dataset.

Key points:
- The model was trained using scaled numerical features
- Churn labels were not used, as clustering is unsupervised

The trained model was saved as a binary file:

- **02_kmeans_model.pkl**

This file stores the trained model and is not readable in a text editor, which is expected behaviour for machine learning models.

---

## 5. Cluster Visualisation and Labelling

### 5.1 Cluster Visualisation
To visually interpret the clustering results, **Principal Component Analysis (PCA)** was applied to reduce the dataset to two dimensions.

The resulting visualisation shows how customers are grouped into different clusters based on similarity.

**Figure 2 below displays the cluster visualisation.**

![Cluster Visualisation](03_cluster_visualization.png)

Each colour represents a different customer cluster.

---

### 5.2 Clustered Dataset
The final output of the clustering process is the clustered dataset:

- **04_clustered_dataset.csv**

This file contains the processed dataset with an additional column representing the **cluster label** assigned to each customer.

---

## 6. Business Insights
The clustering results indicate that customers can be grouped into **distinct segments** with different behaviour and usage patterns.

These segments can be used to:
- Identify high-risk churn groups
- Design targeted retention strategies
- Support personalised marketing and service offerings

---

## 7. Methodological Considerations and Technical Rationale

### 7.1 Categorical Encoding Rationale
Nominal categorical variables such as `InternetService` and `Contract` do not have an inherent ordinal relationship.  
Using Label Encoding for these variables can introduce artificial numerical ordering (for example, Month-to-month < One year < Two year), which may bias distance-based algorithms such as K-Means.

To prevent this issue, **One-Hot Encoding** was applied to all nominal categorical variables used in clustering.  
This ensures that categorical features contribute equally to Euclidean distance calculations without imposing a false numerical hierarchy.

---

### 7.2 Feature Scaling Strategy
K-Means clustering relies on **Euclidean distance**, making feature scaling a critical preprocessing step.  
All continuous numerical features used for clustering were standardised using **StandardScaler** to ensure that no single feature with a larger magnitude disproportionately influenced the clustering process.

This approach improves centroid stability and ensures proportional contribution of all numerical features during cluster formation.

---

### 7.3 Exploratory Data Analysis Prior to Clustering
Prior to clustering, basic **exploratory data analysis (EDA)** was conducted to assess feature distributions, identify potential outliers, and check feature correlations.

- Feature distributions were reviewed using summary statistics and visual inspection.
- Boxplots were examined to identify extreme outliers that could distort centroid placement.
- Correlation analysis was performed to confirm that no highly redundant features dominated the clustering outcome.

No extreme outliers requiring removal were observed, and the selected features were deemed suitable for clustering.

---

### 7.4 Churn Class Balance Consideration
Although clustering is an **unsupervised learning technique** and does not directly use churn labels, class imbalance was reviewed during data preparation. The churn variable was found to be imbalanced, which is typical in telecom datasets.

Since K-Means clustering does not rely on target labels, resampling or class weighting techniques were not applied at this stage.  
Class imbalance will be explicitly addressed during subsequent **supervised churn prediction modelling** stages.

---

### 7.5 Key Technical Decisions Summary
- **One-Hot Encoding** was applied to nominal categorical variables to avoid artificial ordinal relationships.
- **StandardScaler** was used for feature scaling to ensure fair distance-based clustering.
- **Exploratory checks for distributions, outliers, and correlations** were conducted prior to modelling.
- **Churn class imbalance** was acknowledged and deferred to supervised modelling stages.

These decisions were made to ensure methodological correctness, robustness, and interpretability of the clustering analysis.

---

## 8. Conclusion
To conclude, the clustering analysis successfully identified distinct customer segments and provides meaningful insights that can support targeted retention strategies and future churn prediction.  
This completes **Stage 2 of the project**, and all required clustering analysis deliverables have been implemented, documented, and uploaded according to the assessment requirements.  
Thank you.
