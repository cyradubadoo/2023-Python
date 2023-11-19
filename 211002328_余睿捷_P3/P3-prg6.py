#产生两个0～100（包含0和100）的随机整数a和b，求这两个整数的最大公约数和最小公倍数。
import random
m=random.randint(0, 100)
n=random.randint(0, 100)
z=m*n
print(str.format("两个随机数分别为{0} {1}",m,n))
if(m<n):
    m,n=n,m
while(m%n!=0):
    m,n=n,m%n
print(str.format("它们的最大公约数:{0} 最小公倍数:{1}",m,z/n))