# Student Performance Prediction

## Overview

This project predicts student final scores using a Linear Regression model. The dataset contains academic, demographic, and behavioral information about students. The objective is to analyze the factors affecting academic performance and build a machine learning model capable of estimating a student's final score.

---

## Dataset Features

### Input Features

* Gender
* Age
* Study Hours Per Week
* Attendance Rate
* Parent Education Level
* Internet Access
* Participation in Extracurricular Activities
* Previous Academic Score

### Target Variable

* Final Score

---

## Data Preprocessing

The following preprocessing steps were performed:

* Categorical Encoding
* Feature Selection
* Train-Test Split
* Data Validation

Categorical features were converted into numerical values to make them suitable for machine learning algorithms.

---

## Exploratory Data Analysis (EDA)

The following visualizations were generated to understand the dataset:

* Pass/Fail Distribution
* Attendance vs Final Score
* Study Hours vs Final Score
* Final Score Distribution
* Study Hours Distribution
* Internet Access vs Pass/Fail
* Extracurricular Activities vs Pass/Fail
* Average Study Hours by Gender
* Gender vs Pass/Fail
* Average Study Hours by Pass/Fail Status
* Correlation Heatmap

All generated plots are available in the `EDA/` directory.

---

## Machine Learning Model

### Model Used

* Linear Regression

### Evaluation Metrics

* R² Score
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

### Results

| Metric   | Value  |
| -------- | ------ |
| R² Score | 0.7516 |
| MSE      | 53.93  |
| RMSE     | 7.34   |

The model explains approximately 75% of the variation in student final scores and achieves an average prediction error of around 7 marks.

---

## Project Structure

```text
Student-Performance-Prediction/

├── preprocessing.py
├── plots.py
├── linear_regression.py
├── student_performance.csv
├── plots/
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn

---

## Future Improvements

* Decision Tree Regressor
* Random Forest Regressor
* Neural Network Model
* Model Comparison Dashboard
* User Input Based Score Prediction
* Interactive Menu Driven Application

---

## Learning Outcomes

This project demonstrates:

* Data Preprocessing
* Exploratory Data Analysis
* Feature Engineering
* Linear Regression
* Model Evaluation
* Project Modularization in Python

This repository will be expanded with additional machine learning models and model comparison features in future versions.
