import requests
from bs4 import BeautifulSoup

url = 'https://so.gushiwen.org/gushi/tangshi.aspx'

# 使用requests发送HTTP请求
response = requests.get(url)

# 解析HTML页面
soup = BeautifulSoup(response.content, 'html.parser')

# 统计五言绝句、七言绝句、五言律诗等体裁各有多少首诗
wuyan_jueju = len(soup.select('body > div.main3 > div.left > div.sons > div:nth-child(1) > span'))
qiyan_jueju = len(soup.select('body > div.main3 > div.left > div.sons > div:nth-child(2) > span'))
wuyan_lushi = len(soup.select('body > div.main3 > div.left > div.sons > div:nth-child(3) > span'))

print('五言绝句数量：', wuyan_jueju)
print('七言绝句数量：', qiyan_jueju)
print('五言律诗数量：', wuyan_lushi)
