# 输出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值。
import pandas as pd
drinks = pd.read_csv('drinks.csv')
wine_by_continent = drinks.groupby('continent')['wine_servings'].describe()
wine_by_continent = wine_by_continent.round(2)  # 将数值保留两位小数
print(wine_by_continent)