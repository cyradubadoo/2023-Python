'''
编写程序，模拟抓狐狸小游戏。假设一共有一排 5 个洞口，狐狸最开始的时候在其中一个洞口，
然后玩家随机打开一个洞口，如果里面有狐狸就抓到了，如果洞口里没有狐狸就第二天再来抓，
但是第二天狐狸会在玩家来抓之前跳到隔壁洞口里。如果在规定的次数内抓到了狐狸就提前结束游戏并提示成功；
如果规定的次数用完还没有抓到狐狸，就结束游戏并提示失败。'''

import random

def catchfox():
    hole=[0,0,0,0,0]
    m=random.randint(0,4)
    hole[m]=1
    for i in range(5):
        print(f'一共可以抓5次，已抓{i}次.')
        while True:
            try:
                x=input('请输入你要打开的洞口编号（1-5）：')
                x=int(x)
                assert 1<=x<6
                break
            except:
                print('请正确输入洞口编号哦。')
        if hole[x-1]==1:
            print(f'恭喜你！抓到了狐狸！!一共抓了{i+1}次。')
            break
        else:
            hole[m]=0
            if 0<m<4:
                m+=random.choice([-1,1])
            else:
                m+=(1 if m==0 else -1)
            hole[m]=1
            print(f'未抓到狐狸，还有{4-i}次机会')
            if i==4:
                print('机会用光了，未抓到狐狸，游戏结束。')

catchfox()