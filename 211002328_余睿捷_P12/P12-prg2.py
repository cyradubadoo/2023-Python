import matplotlib.pyplot as plt

# 设置字体
plt.rcParams['font.sans-serif'] = ['simsun']

websites = ["亚马逊", "当当网", "中国图书网", "京东", "天猫"]
prices = [39.5, 39.9, 45.4, 38.9, 33.34]

fig, ax = plt.subplots()
ax.barh(websites, prices)
ax.set_title("图书比价")
ax.set_xlabel("价格")
ax.set_ylabel("网站")

# 设置x轴的范围，实现价格区间在40到47之间
plt.xlim(32, 47)

# 对每个柱体添加文本注释，显示数值
for i, v in enumerate(prices):
    ax.text(v + 0.1, i, str(v))

plt.show()
