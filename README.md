# Claorie-prediction
📌 Project Overview

This project builds a machine learning-based system that predicts the number of calories burned during physical exercise using physiological and personal attributes. The model estimates energy expenditure based on inputs such as age, gender, height, weight, workout duration, heart rate, and body temperature.

🎯 Objective

To develop an accurate and data-driven calorie prediction model that improves upon traditional estimation methods by incorporating multiple human physiological factors.

📂 Dataset

The project uses two datasets:

exercise.csv → User exercise & biometric data

calories.csv → Corresponding calories burned

Both datasets were merged to create a unified dataset containing ~15,000 records.

🧹 Data Preprocessing

Checked for missing and duplicate values

Encoded categorical features (Gender)

Normalized numerical variables

Engineered meaningful features:

BMI (Body Mass Index)

Workout Intensity

Temperature Rise per Minute

📊 Exploratory Data Analysis (EDA)

EDA techniques used:

Histograms → Feature distributions

Boxplots → Outlier detection

Correlation Heatmap → Relationship analysis

Key insight: Duration and Heart Rate are the strongest predictors of calorie burn.

🧠 Machine Learning Models

The following regression models were trained and evaluated:

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

Performance measured using:

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² Score

Best Model: Gradient Boosting Regressor

🚀 Deployment

The final model was deployed using Streamlit, allowing users to input workout parameters and receive real-time calorie predictions.

🛠️ Tech Stack

Python

Pandas / NumPy

Scikit-learn

Matplotlib / Seaborn

Streamlit


<img width="1904" height="964" alt="image" src="https://github.com/user-attachments/assets/06ca0d0d-ac9b-47a9-846d-677ca7dc870b" />
