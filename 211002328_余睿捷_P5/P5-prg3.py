#编写程序，删除一个list里面的重复元素。
# 提示：可以利用s.append（x）方法把对象x追加到列表s的尾部。
def delList(L):
    s=[]
    for i in L:
        if i not in s:
            s.append(i)
    return s

print(delList([1,2,3,4,1,2,3,4,5]))
print(delList([1,4,6,8,0,7,4,2,1]))

