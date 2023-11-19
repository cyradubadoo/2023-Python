import requests
from bs4 import BeautifulSoup

url = 'https://so.gushiwen.org/gushi/tangshi.aspx'

# 使用requests发送HTTP请求
response = requests.get(url)

# 解析HTML页面
soup = BeautifulSoup(response.content, 'html.parser')

# 统计唐诗数量
tangshi_count = len(soup.select('body > div.main3 > div.left > div.sons > div.typecont > span'))
print('唐诗数量：', tangshi_count)