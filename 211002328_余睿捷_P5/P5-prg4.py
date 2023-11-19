#编写程序，求列表s=[9，7，8，3，2，1，55，6]中的元素个数、最大值、最小值，以及元素之和、平均值。
# 请思考有哪几种实现方法？提示：可以分别利用for循环、while循环、直接访问列表元素（for i in s…）、
# 间接访问列表元素（for i in range（0，len（s））…）、
# 正序访问（i=0；while i＜len（s）…）、反序访问（i=len（s）-1；while i＞=0…）
# 以及while True：…break等方法。

s=[9,7,8,3,2,1,55,6]
sum=0
num=0
maxnum=max(s)
minnum=min(s)
for i in s:
    num=num+1 #元素个数
    sum=sum+i
    ave=sum/num
print(str("元素个数{0}，最大值{1}，最小值{2}，元素和{3}，平均值{4}").format(num, maxnum, minnum, sum, ave))


