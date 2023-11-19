#编写程序，输入字符串，将其每个字符的ASCII码形成列表并输出。
# 提示：（1）使用ord（s[i]）方法将字符转换为对应的Unicode码。（2）使用s.append（x）方法将对象x追加到列表s的尾部。

s=input('请输入一个字符串：')
l=[]
for i in s:
    l.append(ord(i))
print(l)
