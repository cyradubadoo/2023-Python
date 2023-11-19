import math
r=float(input("请输入球的半径："))
s=4*math.pi*r**2
v=4*math.pi*r**3/3

print(str.format("球的表面积为：{0:2.2f}，体积为：{1:2.2f}",s,v))