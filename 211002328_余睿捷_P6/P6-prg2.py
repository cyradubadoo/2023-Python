#编写函数求三个整数的最大值。
def max3(a,b,c):
    if(a>b):
        max=a
    else:
        max=b
    if(max>c):
        max=max
    else:
        max=c;
    print("三者中最大的值为",max)

x=int(input("请输入第一个数："))
y=int(input("请输入第二个数："))
z=int(input("请输入第三个数："))
max3(x,y,z)
