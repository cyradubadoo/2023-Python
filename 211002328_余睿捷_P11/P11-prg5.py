# 输出每个大陆每种酒类别的消耗平均值和中位数。
import pandas as pd
drinks = pd.read_csv('drinks.csv')
drinks_by_continent=drinks.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].agg(['mean','median'])
drinks_by_continent = drinks_by_continent.round(2)  # 将数值保留两位小数
pd.set_option('display.max_columns', None) # 显示所有列
print(drinks_by_continent)
