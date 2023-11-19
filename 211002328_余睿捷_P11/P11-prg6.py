# 输出每个大陆对spirit饮品消耗的平均值、最大值和最小值。
import pandas as pd
drinks = pd.read_csv('drinks.csv')
spirit_by_continent = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'max', 'min'])
spirit_by_continent = spirit_by_continent.round(2)  # 将数值保留两位小数
print(spirit_by_continent)