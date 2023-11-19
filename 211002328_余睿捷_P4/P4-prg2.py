#编写程序，格式化输出杨辉三角。杨辉三角即二项式定理的系数表，各元素满足如下条件：
# 第一列及对角线上的元素均为1；其余每个元素等于它上一行同一列元素与前一列元素之和。
#提示：可以使用“print（＂1＂.center（20））”的语句形式在一行上打印20个字符，并且居中对齐。
num = int(input("请输入行数:"))

def triangle():
    m = [1]
    while True:
        yield m
        m = [1] + [m[i] + m[i + 1] for i in range(len(m) - 1)] + [1]

n = 0
for i in triangle():
    print(str(i).center(100))
    n = n + 1
    if n == num:
        break
