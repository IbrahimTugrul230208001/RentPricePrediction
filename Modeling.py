from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV,KFold
import pandas as pd
import xgboost as xgb

df = pd.read_csv("Ankara Rent Prices/modeling_data.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

X= df.drop('Price',axis=1)
y = df['Price']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)


# Define the model

rf = RandomForestRegressor(bootstrap=True,max_depth=10,max_features='log2',min_samples_leaf=1,min_samples_split=5,n_estimators=200)
rf.fit(X_train,y_train)


y_pred = rf.predict(X_test)
score = r2_score(y_test,y_pred)

print(score)

#0.9412...
"""
# Make predictions

y_pred = model.predict(X_test)


# Create a DataFrame for comparison
comparison = pd.DataFrame({
    "actual": y_test,
    "prediction": y_pred
})

# Set up k-fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Evaluate the model using cross-validation
cv_scores = cross_val_score(model, X, y, cv=kf, scoring='r2')

# Print the results
print(f'Cross-Validation R² Scores: {cv_scores}')
print(f'Mean R² Score: {cv_scores.mean()}')
print(comparison.head(50))
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2'],
    'bootstrap': [True, False]
}
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, 
                           scoring='neg_mean_squared_error', 
                           cv=5, n_jobs=-1, verbose=2)

grid_search.fit(X_train, y_train)
print(grid_search.best_params_)





# Define the grid of hyperparameters
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, 10],
    'learning_rate': [0.01, 0.1, 0.3],
    'subsample': [0.6, 0.8, 1.0],
    'max_features': ['auto', 'sqrt', 'log2']
}

# Set up GridSearchCV
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='r2', cv=5, n_jobs=-1, verbose=2)

# Fit the grid search to the data
grid_search.fit(X_train, y_train)

# Print the best parameters and the corresponding score
print("Best parameters found: ", grid_search.best_params_)
print("Best R² score: ",grid_search.best_score_)



rf = RandomForestRegressor(bootstrap=True,max_depth=10,max_features='log2',min_samples_leaf=1,min_samples_split=5,n_estimators=200)
rf.fit(X_train,y_train)

GBoost = GradientBoostingRegressor(learning_rate=0.1,max_depth=5,max_features='sqrt',n_estimators=50,subsample=1.0)
GBoost.fit(X_train,y_train)
"""