import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score 
from preprocessing import encode_data
df = pd.read_csv("student_performance.csv")
df = encode_data(df)

def train_linear_regression(X_train,X_test,y_train):
    model = LinearRegression()
    model.fit(X_train,y_train)

    y_pred = model.predict(X_test)

    return model,y_pred

X = df.drop(
        ["student_id","passed","final_score"],
        axis = 1
    )
y = df["final_score"]
X_train,X_test,y_train,y_test = train_test_split(
    X,y,
    test_size = 0.2,
    random_state = 42
)
model,y_pred = train_linear_regression(X_train,X_test,y_train)

print("R2 Score:",r2_score(y_test,y_pred))
print("MSE: ",mean_squared_error(y_test,y_pred))
rmse = mean_squared_error(
    y_test,
    y_pred
) ** 0.5

print("RMSE:", rmse)
plt.figure(figsize=(8,5))

plt.scatter(
    y_test,
    y_pred
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)

plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Actual vs Predicted Scores")

plt.show()