# Student Performance Prediction

## Overview

This project predicts student final scores using Machine Learning techniques. The dataset contains academic, demographic, and behavioral information about students. The objective is to analyze the factors influencing academic performance and build predictive models capable of estimating a student's final score.

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
* Train / Validation / Test Splitting
* Data Validation

Categorical variables were converted into numerical values to make them suitable for machine learning models.

---

## Exploratory Data Analysis (EDA)

The following visualizations were generated:

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

## Machine Learning Models

### 1. Linear Regression

#### Evaluation Metrics

| Metric   | Value  |
| -------- | ------ |
| R² Score | 0.7516 |
| MSE      | 53.93  |
| RMSE     | 7.34   |

#### Observation

Linear Regression explains approximately 75% of the variation in student final scores and achieves the best performance among the currently implemented models.

---

### 2. Decision Tree Regressor

#### Hyperparameter Tuning

The following hyperparameters were tuned using a validation set:

* Maximum Tree Depth
* Minimum Samples Split
* Minimum Samples Leaf

Best Parameters:

* max_depth = 4
* min_samples_split = 15
* min_samples_leaf = 1

#### Evaluation Metrics

| Metric   | Value  |
| -------- | ------ |
| R² Score | 0.6591 |
| MSE      | 87.65  |
| RMSE     | 9.36   |

#### Observation

The Decision Tree Regressor performed worse than Linear Regression on this dataset, suggesting that the relationship between the features and target variable is predominantly linear.

---

## Model Comparison

| Model                   | R² Score | RMSE |
| ----------------------- | -------- | ---- |
| Linear Regression       | 0.7516   | 7.34 |
| Decision Tree Regressor | 0.6591   | 9.36 |

---

## Project Structure

```text
Student-Performance-Prediction/

├── preprocessing.py
├── plots.py
├── linear_regression.py
├── decision_tree.py
├── student_performance.csv
├── EDA/
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

---

## Future Improvements

* Random Forest Regressor
* Neural Network Model
* User Input Based Score Prediction

---

## Learning Outcomes

This project demonstrates:

* Data Preprocessing
* Exploratory Data Analysis
* Feature Engineering
* Linear Regression
* Decision Tree Regression
* Hyperparameter Tuning
* Model Evaluation
* Python Project Modularization
* Git and GitHub Version Control

---

## Conclusion

Among the models implemented so far, Linear Regression achieved the best performance with an R² score of 0.7516. The results suggest that student final scores in this dataset exhibit a strong linear relationship with the selected features.

The project will continue to evolve with additional machine learning models and performance comparisons.
