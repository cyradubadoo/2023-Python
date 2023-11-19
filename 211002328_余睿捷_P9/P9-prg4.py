import requests
from bs4 import BeautifulSoup

url = 'https://so.gushiwen.org/gushi/tangshi.aspx'

# 使用requests发送HTTP请求
response = requests.get(url)

# 解析HTML页面
soup = BeautifulSoup(response.content, 'html.parser')

# 统计入选唐诗三百首最多的前10个诗人
author_dict = {}
for author in soup.select('body > div.main3 > div.left > div.sons > div.typecont > span'):
    # author_name = author.text.strip()
    try:
        author_name = author.contents[1].strip("()")
    except IndexError:
        author_name = ""
    # print(author_name)

    if author_name in author_dict:
        author_dict[author_name] += 1
    else:
        author_dict[author_name] = 1

top10_authors = sorted(author_dict.items(), key=lambda x: x[1], reverse=True)[:10]

# 输出结果
print('入选唐诗三百首最多的前10个诗人：')
for author, count in top10_authors:
    print(author, count)

