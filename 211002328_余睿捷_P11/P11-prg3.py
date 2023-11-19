# 输出每个大陆(continent)平均消耗的啤酒(beer)量。
import pandas as pd
drinks = pd.read_csv('drinks.csv')
beer_by_continent = drinks.groupby('continent')['beer_servings'].mean()
beer_by_continent = beer_by_continent.round(2)  # 将数值保留两位小数
print(beer_by_continent)