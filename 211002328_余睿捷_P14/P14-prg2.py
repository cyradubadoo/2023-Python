import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 数据探索和准备
data = pd.read_csv('pimaindiansdiabetes.csv', header=None)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化模型
lr = LogisticRegression()
knn = KNeighborsClassifier()
dt = DecisionTreeClassifier()
nb = GaussianNB()
svm = SVC()

# 训练模型并预测
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)

svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)

# 评估模型性能
accuracy_lr = accuracy_score(y_test, y_pred_lr)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
accuracy_dt = accuracy_score(y_test, y_pred_dt)
accuracy_nb = accuracy_score(y_test, y_pred_nb)
accuracy_svm = accuracy_score(y_test, y_pred_svm)

print(f"Logistic Regression accuracy: {accuracy_lr}")
print(f"KNN accuracy: {accuracy_knn}")
print(f"Decision Tree accuracy: {accuracy_dt}")
print(f"Naive Bayes accuracy: {accuracy_nb}")
print(f"SVM accuracy: {accuracy_svm}")

# 可视化分类器的性能
classifiers = ['Logistic Regression', 'KNN', 'Decision Tree', 'Naive Bayes', 'SVM']
accuracies = [accuracy_lr, accuracy_knn, accuracy_dt, accuracy_nb, accuracy_svm]

plt.bar(classifiers, accuracies)
plt.xlabel('Classifier')
plt.ylabel('Accuracy')
plt.title('Classifier Performance on Pima Indians Diabetes Dataset')
plt.show()