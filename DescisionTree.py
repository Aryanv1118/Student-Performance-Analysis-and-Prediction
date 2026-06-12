import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import GridSearchCV
from preprocessing import encode_data
df = pd.read_csv("student_performance.csv")
df = encode_data(df)

def tune_descision_tree(X_train,y_train,X_cv,y_cv):
    best_score = float('-inf')
    best_depth = 0
    for depth in range(1,16):
        model = DecisionTreeRegressor(
            max_depth = depth,
            random_state = 42
        )
        model.fit(X_train,y_train)
        y_pred = model.predict(X_cv)
        score = r2_score(y_cv,y_pred)
        if(score>best_score):
            best_score = score
            best_depth = depth
    best_score = float('-inf')
    best_min_sample_split = 0
    for split in [2,5,10,15,20]:
        model = DecisionTreeRegressor(
            max_depth = best_depth,
            min_samples_split = split,
            random_state = 42
        )
        model.fit(X_train,y_train)
        y_pred = model.predict(X_cv)
        score = r2_score(y_cv,y_pred)
        if(score>best_score):
            best_score = score
            best_min_sample_split = split
    best_score = float('-inf')
    best_min_sample_leaf = 0
    for leaf in [1, 2, 5, 10, 15, 20]:
        model = DecisionTreeRegressor(
            max_depth = best_depth,
            min_samples_split = best_min_sample_split,
            min_samples_leaf = leaf,
            random_state = 42
        )
        model.fit(X_train,y_train)
        y_pred = model.predict(X_cv)
        score = r2_score(y_cv,y_pred)
        if(score>best_score):
            best_score = score
            best_min_sample_leaf = leaf
    return best_depth,best_min_sample_split,best_min_sample_leaf
def descision_tree_regression(X_train,y_train,X_test,depth,sample_split,sample_leaf):
    model = DecisionTreeRegressor(
        max_depth = depth,
        min_samples_split = sample_split,
        min_samples_leaf = sample_leaf,
        random_state = 42
    )
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    return model,y_pred
X = df.drop(
        ["student_id","passed","final_score"],
        axis = 1
    )
y = df["final_score"]
X_train,X_temp,y_train,y_temp = train_test_split(X,y,test_size=0.4,random_state=42)
X_cv,X_test,y_cv,y_test = train_test_split(X_temp,y_temp,test_size=0.5,random_state=42)
depth,split,leaf = tune_descision_tree(X_train,y_train,X_cv,y_cv)
X_train_final = pd.concat([X_train, X_cv])
y_train_final = pd.concat([y_train, y_cv])
model, y_pred = descision_tree_regression(
    X_train_final,
    y_train_final,
    X_test,
    depth,
    split,
    leaf
)
print("\n===== Manual Tuning =====")
print("Best Depth:", depth)
print("Best Split:", split)
print("Best Leaf:", leaf)
print("R2 Score:",r2_score(y_test, manual_pred))
print("MSE:",mean_squared_error(y_test, manual_pred))
manual_rmse = mean_squared_error(y_test,manual_pred) ** 0.5
print("RMSE:", manual_rmse)
