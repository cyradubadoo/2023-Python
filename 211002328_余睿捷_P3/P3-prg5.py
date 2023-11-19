#输入一元二次方程的3个系数a、b和c，求ax 2 +bx+c=0方程的解。
import math
a=float(input("请输入系数a:"))
b=float(input("请输入系数b:"))
c=float(input("请输入系数c:"))
judge=b**2-4*a*c
if(a==0):
    if(b==0):print("无解")
    else:
        x1=-c/b
        print("有一个实根：",x1)
elif(judge==0):
    x1=(-b)/(2*a)
    print("有两个相等实根：",x1)
elif(judge>0):
    x1=(-1*b+math.sqrt(judge))/2*a
    x2=(-1*b-math.sqrt(judge))/2*a
    print(str.format("有两个不等实根：{0} 和 {1}",x1,x2))
elif(judge<0):
    x1=(-1*b)/(2*a)
    x2=math.sqrt(judge*-1)/(2*a)
    print(str.format("有两个不等虚根：{0}+{1}i 和 {0}-{1}i",x1,x2))