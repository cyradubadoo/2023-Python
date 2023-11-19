import requests
from lxml import etree
import os

# 发送HTTP请求获取页面内容
url = 'https://www.cae.cn/cae/html/main/col48/column_48_1.html'
response = requests.get(url)
html = response.content.decode('utf-8')
# 解析HTML
tree = etree.HTML(html)

# 使用XPath表达式获取每位院士的姓名和链接，并保存到字典中。
# 获取每位院士的姓名和链接
academicians = {}
academicians_elem = tree.xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/ul/li[@class="name_list"]/a')
# wenti3 '/html/body/div[3]/div/div[2]/div/div[2]/div/ul/li/a'
for elem in academicians_elem:
    name = elem.text
    link = elem.get('href')
    # academicians.append({'name': name, 'link': link}) wenti1
    academicians[name] = link
count = 0
# 遍历字典中每位院士的链接，获取每位院士的简介和照片，并保存到本地文件中。
# 遍历每位院士的链接，获取简介和照片
for name, link in academicians.items():
    # 发送HTTP请求获取院士页面内容
    response = requests.get('https://www.cae.cn/' + link)  # wenti4 'https://www.cae.cn/' +
    html = response.content.decode('utf-8')
    tree = etree.HTML(html)

    # 获取院士简介
    # intro = tree.xpath('//div[@class="intro"]/p/text()')
    intro = tree.xpath('/html/body/div[3]/div/div[3]/div[2]/p/text()')  # wenti2 /p
    intro = ''.join(intro).strip()

    # 获取院士照片
    # img_url = tree.xpath('//div[@class="intro"]/div[@class="pic"]/a/img/@src')[0]
    img_url = tree.xpath('/html/body/div[3]/div/div[3]/div[1]/a/img/@src')[0]
    img_content = requests.get('https://www.cae.cn/' + img_url).content


    count = count + 1

    # 创建文件夹（如果不存在）
    if not os.path.exists('academicians'):
        os.mkdir('academicians')

    # 保存院士简介到文本文件
    with open(f'academicians/{name}.txt', 'w', encoding='utf-8') as f:
        f.write(intro)
    # 保存院士照片到图片文件
    with open(f'academicians/{name}.jpg', 'wb') as f:
        f.write(img_content)

print(count)
