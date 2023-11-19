# 输入：两个整数（不大于4和3），中间以空格分开
# 输出：这两个整数的参数值

def A(m,n):
    if(m==0):
        return n+1
    elif(n==0):
        return A(m-1,1)
    else:
        return A(m-1,A(m,n-1))

print("请输入两个整数（不大于4和3），中间以空格分开")
a,b=map(int, input().split())
print(A(a,b))
