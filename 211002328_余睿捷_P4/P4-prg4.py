#编程实现袖珍计算器，要求输入两个操作数和一个操作符（+、-、*、/、%），
# 根据操作符输出运算结果。注意“/”和“%”运算符的零除异常问题。
m = float(input("请输入第一个操作数："))
operator = input("请输入操作符（+、-、*、/、%）：")
n = float(input("请输入第二个操作数："))

if (n == 0 and (operator == '/' or operator == '%')):
    print("运算符零除异常")

else:
    if operator == '+':
        result = m + n
    elif operator == '-':
        result = m - n
    elif operator == '*':
        result = m * n
    elif operator == '/':
        result = m / n
    elif operator == '%':
        result = m % n
print(result)