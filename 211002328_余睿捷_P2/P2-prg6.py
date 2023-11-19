#提示输入姓名和出生年份，输出姓名和年龄。
#提示：（1）用户可以使用datetime.date.today（）.year返回当年的年份值。
# （2）用户可以使用“print（＂您好！{0}。您{1}岁。＂.format（sName，age））”的语句形式输出程序运行效果。

import datetime
sName=str(input("请输入姓名："))
year=int(input("请输入出生年份："))
age=datetime.date.today().year-year
print("您好！{0}。您{1}岁。".format(sName,age))
