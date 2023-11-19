#统计所输入字符串中单词的个数，单词之间用空格分隔。
def word_len(s):
    return len([i for i in s.split(' ')])

s =  str(input("请输入字符串："))
l = word_len(s)
print(f'一共有{l}个单词。')

