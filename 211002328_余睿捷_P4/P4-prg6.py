#一球从100米的高度自由落下，每次落地后反弹回原高度的一半，再落下。
# 求小球在第10次落地时共经过多少米？第10次反弹多高？
sum = 0
height = 100
up = 0

for i in range(1, 11):
    sum += height + up
    height = up = height / 2

print("小球在第十次落地时共经过:{0}米，第十次反弹高度:{1}米".format(sum, height))