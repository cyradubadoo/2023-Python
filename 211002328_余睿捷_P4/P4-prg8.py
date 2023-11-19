#求Sn=a+aa+aaa+…+aa…aaa（有n 个a）之值，其中a 是一个数字。
# 在本题中， a＝2。 例如：2+22+222+2222+22222（n=5），n 由键盘输入。
# 要求：利用字符串的乘法实现。
#a=int(input("请输入a的值："))
n=int(input("请输入n的值："))
import random
a = 2
s = 0
for i in range(1, n + 1):
    s += a
    a = 10 * a + 2

print("Sn = {0}".format(s))