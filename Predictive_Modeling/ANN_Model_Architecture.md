# ANN Model Architecture – Customer Churn Prediction

## Model Overview
An Artificial Neural Network (ANN) model was developed to predict telecom customer churn using customer demographic, service usage, and billing information.

The objective of the model is to classify whether a customer will churn (leave the service) or remain with the telecom provider.

---

## Model Architecture

Input Layer  
The input layer receives customer features from the processed telecom churn dataset.

Hidden Layer 1  
Dense neural network layer using ReLU activation function to learn nonlinear patterns in the data.

Hidden Layer 2  
Another dense layer using ReLU activation to further extract complex feature relationships.

Output Layer  
A single neuron with Sigmoid activation function is used to perform binary classification:

0 = Customer stays  
1 = Customer churns

---

## Training Configuration

Optimizer  
Adam optimizer was used to efficiently update model weights during training.

Loss Function  
Binary Cross Entropy was used since the problem is a binary classification task.

Evaluation Metrics  
Model performance was evaluated using:

• Accuracy  
• Confusion Matrix  
• Training and Validation Loss  
• Training and Validation Accuracy

---

## Model Performance

The trained ANN model achieved an approximate prediction accuracy of **78%** on the test dataset.

The confusion matrix and training graphs provide insights into the model’s predictive performance.