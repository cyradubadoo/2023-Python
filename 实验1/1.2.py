'''
编写程序,读取 Word 文件中的所有段落文本，然后输出其中所有红色的文本和
加粗的文本以及同时具有这两种属性的文本。具体步骤如下：
1.在命令提示符环境使用 pip install python-docx 命令安装扩展库python-docx。
2.创建测试用的 Word 文档 test.docx，写入测试内容，并根据需要设置红色文本和加粗文本。
3.编写程序查找并输出 Word 文档 test.docx 中的红色文本和加粗文本。'''
from docx import Document
from docx.shared import RGBColor

boldText = []
redText = []
doc = Document('test.docx')
for p in doc.paragraphs:
    for r in p.runs:
        # 加粗字体
        if r.bold:
            boldText.append(r.text)
        # 红色字体
        if r.font.color.rgb == RGBColor(255, 0, 0):
            redText.append(r.text)

result = {'red text': redText,
          'bold text': boldText,
          'both': set(redText) & set(boldText)}

for title in result.keys():
    print(title.center(30, '='))
    for text in result[title]:
        print(text)