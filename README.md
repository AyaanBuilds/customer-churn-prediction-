# Customer Churn Prediction System 📊

A Machine Learning-based **Customer Churn Prediction System** that predicts whether a customer is likely to leave a company based on their demographic, service usage, account, and billing information.

The project demonstrates a complete machine learning workflow, including **data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and prediction**.

---

## 🚀 Project Overview

Customer churn is a major challenge for businesses, especially in industries such as telecommunications, banking, SaaS, and subscription-based services.

This project uses historical customer data to identify patterns associated with customer churn and builds a classification model that predicts whether a customer is likely to **churn** or **stay**.

### Problem Statement

> Given customer information and service-related features, predict whether the customer will leave the company.

### Objective

* Analyze customer behavior and churn patterns
* Preprocess and clean customer data
* Identify important features affecting churn
* Train machine learning classification models
* Evaluate model performance
* Predict churn for new customers

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* **Pandas** — Data manipulation and analysis
* **NumPy** — Numerical computations
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **Scikit-learn** — Machine learning and preprocessing
* **Joblib** — Saving and loading trained models

---

## 📂 Project Structure

```text
customer-churn-prediction/
│
├── data/
│   └── customer_churn.csv
│
├── notebooks/
│   └── customer_churn_analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── models/
│   └── churn_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact structure can be modified depending on how the project is organized.

---

## 📊 Dataset

The dataset contains customer-related information such as:

| Feature          | Description                              |
| ---------------- | ---------------------------------------- |
| Customer ID      | Unique customer identifier               |
| Gender           | Customer gender                          |
| Senior Citizen   | Whether the customer is a senior citizen |
| Partner          | Whether the customer has a partner       |
| Dependents       | Whether the customer has dependents      |
| Tenure           | Number of months with the company        |
| Internet Service | Type of internet service                 |
| Contract         | Customer contract type                   |
| Payment Method   | Customer payment method                  |
| Monthly Charges  | Monthly amount paid                      |
| Total Charges    | Total amount charged                     |
| Churn            | Whether the customer left the company    |

The **Churn** column is the target variable.

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Encoding Categorical Features
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Churn Prediction
```

---

## 🧹 Data Preprocessing

The following preprocessing techniques are applied:

* Handling missing values
* Removing unnecessary columns
* Converting data types
* Encoding categorical variables
* Separating features and target variable
* Splitting data into training and testing sets
* Feature scaling where required

Example:

```python
X = df.drop("Churn", axis=1)
y = df["Churn"]
```

---

## 🤖 Machine Learning Models

The project can evaluate multiple classification algorithms, such as:

### 1. Logistic Regression

Used as a baseline classification model.

### 2. Decision Tree Classifier

Captures non-linear relationships between customer features and churn.

### 3. Random Forest Classifier

Uses multiple decision trees to improve predictive performance and reduce overfitting.

---

## 📈 Model Evaluation

The models are evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

Example:

```text
              precision    recall    f1-score

No Churn         XX         XX         XX
Churn            XX         XX         XX

Accuracy                    XX
```

> Replace `XX` with the actual results obtained from your trained models.

---

## 🔮 Prediction

After training, the model can be used to predict churn for a new customer.

Example:

```python
prediction = model.predict(customer_data)

if prediction[0] == 1:
    print("Customer is likely to churn")
else:
    print("Customer is likely to stay")
```

---

## 💡 Business Use Case

A company can use this system to identify customers who have a high probability of leaving.

The business can then take actions such as:

* Offering personalized discounts
* Providing better support
* Offering suitable plans
* Improving customer experience
* Creating customer retention campaigns

The model therefore helps convert customer data into actionable insights.

---

## 📊 Future Improvements

Possible improvements to this project include:

* Hyperparameter tuning
* Cross-validation
* Feature importance analysis
* Handling class imbalance using techniques such as SMOTE
* Comparing additional ML algorithms
* Building an interactive Streamlit web application
* Deploying the model using Flask or FastAPI
* Adding a customer churn probability score
* Creating a dashboard for business users

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
```

Navigate to the project directory:

```bash
cd customer-churn-prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the training script:

```bash
python src/train.py
```

Run the prediction script:

```bash
python src/predict.py
```

If the project includes a Jupyter Notebook, open:

```bash
jupyter notebook
```

and run the cells sequentially.

---

## 📦 Requirements

Example `requirements.txt`:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
```

---

## 🎯 Key Learning Outcomes

Through this project, I learned and implemented:

* Data preprocessing
* Exploratory Data Analysis
* Categorical feature encoding
* Feature scaling
* Classification algorithms
* Train-test splitting
* Model evaluation
* Confusion matrix analysis
* Model comparison
* Model persistence using Joblib
* End-to-end machine learning workflow


