#计算2+4+6+8…+100之和。
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print("2+4+6+..+100的和为",sum)