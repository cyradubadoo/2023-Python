# 将数据框命名为drinks，并输出前5行数据。
import pandas as pd
drinks = pd.read_csv('drinks.csv')
pd.set_option('display.max_columns', None) # 显示所有列
print(drinks.head())