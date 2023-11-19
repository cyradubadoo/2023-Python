price=int(input("请输入本金："))
rate=float(input("请输入年利率："))
num=int(input("请输入年数："))
amount=price*(1+rate)**num

print(str.format("本金利率和为：{0:2.2f}",amount))