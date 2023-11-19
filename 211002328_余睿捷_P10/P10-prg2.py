import numpy as np

# 设置打印数的小数点只有两位
np.set_printoptions(precision=2)

# 创建10x10的随机数组
# arr = np.random.rand(10, 10)
arr = np.random.uniform(low=0.00, high=100.00, size=(10, 10))
print("随机数组：")
print(arr)

# 找到最大值和最小值
max_val = arr.max()
min_val = arr.min()

print("最大值：", max_val)
print("最小值：", min_val)
