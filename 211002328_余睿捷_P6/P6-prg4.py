#列表L= [(92,88), (79,99), (84,92), (66, 77)]有4项数据，每项数据表示学生的语文和数学成绩。
# 求数学成绩最高的学生的成绩。提示：应用max函数，然后设计lambda函数来实现，
# max(L, key=lambda ________ )。

L= [(92,88), (79,99), (84,92), (66, 77)]
x=max(L,key = lambda L:L[1])
print(x)