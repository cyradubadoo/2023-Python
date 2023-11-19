import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV

# 1. 数据探索和准备
data = pd.read_csv('winequalitywhite.csv', sep=';')
X = data.drop('quality', axis=1)
y = data['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 2. 训练模型
models = {
    'Logistic Regression': LogisticRegression(),
    'Ridge Regression': Ridge(),
    'Lasso Regression': Lasso(),
    'Elastic Net Regression': ElasticNet(),
    'KNN': KNeighborsRegressor(),
    'Decision Tree': DecisionTreeRegressor(),
    'SVM': SVR()
}
params = {
    'Logistic Regression': {'C': [0.1, 1, 10]},
    'Ridge Regression': {'alpha': [0.1, 1, 10]},
    'Lasso Regression': {'alpha': [0.1, 1, 10]},
    'Elastic Net Regression': {'alpha': [0.1, 1, 10], 'l1_ratio': [0.2, 0.5, 0.8]},
    'KNN': {'n_neighbors': [5, 10, 20]},
    'Decision Tree': {'max_depth': [5, 10, 20]},
    'SVM': {'C': [0.1, 1, 10], 'kernel': ['linear', 'poly', 'rbf']}
}

results = {}
for name, model in models.items():
    clf = GridSearchCV(model, params[name], cv=5, scoring='neg_mean_squared_error')
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    results[name] = {
        'MSE': mean_squared_error(y_test, y_pred),
        'MAE': mean_absolute_error(y_test, y_pred),
        'R2': r2_score(y_test, y_pred)
    }
    print(name, 'MSE:', results[name]['MSE'], 'MAE:', results[name]['MAE'], 'R2:', results[name]['R2'])
