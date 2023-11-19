#计算S n =1+1/2+1/3+…。
import math
sum=0;i=1
while(1/i>=pow(10,-6)):
    sum=sum+1/i
    i=i+1
print(sum)