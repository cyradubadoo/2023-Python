import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取文本文件
text = open('../211002328_余睿捷_P12/中国制造2025.txt', encoding='utf-8').read()

# 中文分词
text = ' '.join(jieba.cut(text))

# 生成词云图
wc = WordCloud(font_path='../211002328_余睿捷_P12/simsun.ttf', background_color='white').generate(text)

# 显示词云图
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
