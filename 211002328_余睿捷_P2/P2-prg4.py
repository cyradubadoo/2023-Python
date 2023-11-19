#声明函数getValue（b，r，n），
#根据本金b、年利率r和年数n计算最终收益v，v=b(1+r)n ；
#然后编写测试代码，提示输入本金、年利率和年数，显示最终收益（保留两位小数）。

def getValue(b,r,n):
    v = b*((1+r)**n)
    return v
nb = float(input("请输入本金："))
nr = float(input("请输入年利率："))
ny = int(input("请输入年份："))
print(str.format("最终收益为：{0:2.2f}",getValue(nb,nr,ny)))