#输入两个正整数m和n（m），求m到n之间（包括m和n）所有素数的和，
# 要求定义并调用函数is_prime(x)来判断x是否为素数。
# 例如，输入1和10，那么这两个数之间的素数有2、3、5、7，其和是17。
def is_prime(x):
    for i in range(2,x):
        if(x%i)==0:
            return 0
    return x

def main():
    m=int(input("请输入第一个正整数："))
    n=int(input("请输入第二个正整数："))
    sum=0
    for j in range(m,n+1):
        sum+=is_prime(j)
    print('{0}和{1}之间素数之和为{2}'.format(m,n,sum))

main()





