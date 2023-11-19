#输入三角形的3条边，先判断是否可以构成三角形，
# 如果可以，则进一步求三角形的周长和面积，否则报错“无法构成三角形！”，结果均保留一位小数。
import math
a=float(input("请输入三角形的边长a:"))
b=float(input("边长b:"))
c=float(input("边长c:"))
if a+b>c and a+c>b and b+c>a:
    h=(a+b+c)/2
    S=math.sqrt(h*(h-a)*(h-b)*(h-c));
    C=2*h;
    print(str.format("三角形的周长和面积分别为:{0}，{1}",C,S))
else:
    print("无法构成三角形.")