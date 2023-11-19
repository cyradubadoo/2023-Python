from sklearn.datasets import load_iris
import numpy as np

# 加载iris数据集
iris = load_iris()

# 设置打印数的小数点只有两位
np.set_printoptions(precision=2)

# 查看数据集中二维数组的形状
print("数据集中包含了{}行{}列的数据。".format(*iris.data.shape))

# 查看二维数组的数据类型
print("数据类型：", iris.data.dtype)

# 求每列的最大值、最小值和平均值
max_vals = np.max(iris.data, axis=0)
min_vals = np.min(iris.data, axis=0)
mean_vals = np.mean(iris.data, axis=0)

print("每列的最大值：", max_vals)
print("每列的最小值：", min_vals)
print("每列的平均值：", mean_vals)
