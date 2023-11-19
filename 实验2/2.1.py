# (1)tkinter 小学数学口算题生成器

import tkinter as tk
from tkinter import ttk
import os
import random
from docx import Document

# 创建题目生成器类
class MathQuizGenerator:
    def __init__(self, master):
        # 初始化主窗口
        self.master = master
        self.master.title("小学口算题生成器")  # 设置窗口标题
        self.master.geometry("350x100")  # 设置窗口大小
        self.create_widgets()  # 调用创建控件的方法

    def create_widgets(self):
        # 创建下拉菜单和输入框等控件
        grade_label = tk.Label(self.master, text="Grade：")  # 创建标签控件，显示年级
        options = ["1", "2", "3", "4", "5", "6"]  # 创建下拉菜单的选项
        self.grade_combo = ttk.Combobox(self.master, values=options, width=7)  # 创建下拉菜单控件，显示选项
       
        num_label = tk.Label(self.master, text="Number：")  # 创建标签控件，显示题目数量
        self.num_entry = tk.Entry(self.master, width=10)  # 创建文本框控件，输入题目数量

        grade_label.grid(row=0, column=0)  # 将年级标签控件放置在窗口中的第一行第一列
        self.grade_combo.grid(row=0, column=1)  # 将下拉菜单控件放置在窗口中的第一行第二列
        num_label.grid(row=0, column=4)  # 将题目数量标签控件放置在窗口中的第一行第五列
        self.num_entry.grid(row=0, column=5)  # 将文本框控件放置在窗口中的第一行第六列

        # 创建生成题目按钮
        self.generate_button = tk.Button(self.master, text="GO", command=self.generate_quiz)  # 创建按钮控件，点击生成题目
        self.generate_button.grid(row=1, column=2, padx=5, pady=5)  # 将按钮控件放置在窗口中的第二行第三列，并添加一些内边距

    def generate_quiz(self):
        # 获取用户选择的年级、题目数量和输出格式
        grade = int(self.grade_combo.get())  # 获取下拉菜单中选择的年级
        num = int(self.num_entry.get())  # 获取文本框中输入的题目数量

        # 根据年级设置运算符和数字范围
        if grade < 3:
            operators = '+-'  # 一年级和二年级只有加减法
            Max = 20  # 数字范围在20以内
        elif grade <= 4:
            operators = '＋－×÷'  # 三年级和四年级有加减乘除法
            Max = 100  # 数字范围在100以内
        elif grade <= 6:
            operators = '＋－×÷('  # 五年级和六年级加减乘除和括号都有
            Max = 100  # 数字范围在100以内
        
        # 创建一个新的word文档对象
        document = Document()
        # 创建一个表格，行数为题目数量除以4，列数为4
        table = document.add_table(rows=num//4, cols=4)

        # 循环生成题目并填充到表格中
        for row in range(num//4):
            for col in range(4):
                # 随机生成两个数和一个运算符
                first = random.randint(1,Max)
                second = random.randint(1,Max)
                operator = random.choice(operators)

                if operator != '(':  # 如果不是五年级
                    if operator == '-'or'÷':    # 如果是减法或除法，确保第一个数大于等于第二个数
                        if first < second:
                            first,second = second,first   
                    # 格式化题目字符串
                    r = str(first).ljust(2,' ')+' ' + operator + str(second).ljust(2,' ') + '='
                                
                else:  # 如果是五年级 
                    third = random.randint(1,100)  # 随机生成第三个操作数
                    while True:  # 随机生成两个操作符
                        o1 = random.choice(operators)
                        o2 = random.choice(operators)
                        if o1 != '(' and o2 !='(':
                            # 如果两个操作符均不为左括号，则跳出循环
                            break
                    # 考虑括号的口算题
                    r2 = random.randint(1,100)
                    if r2 > 50:
                        if o2 == '-':  # 如果第二个操作数小于第三个操作数，则交换它们的值
                            if second < third:
                                second,third = third,second
                        # 格式化题目字符串
                        r = str(first).ljust(2,' ') + o1 +'('+str(second).ljust(2,' ')+o2+str(third).ljust(2,' ')+')='
                    else:
                        if o1 == '-':
                            if first < second:  # 如果第一个操作数小于第二个操作数，则交换它们的值
                                first,second = second,first
                        # 格式化题目字符串
                        r = '(' + str(first).ljust(2,' ') + o1 +str(second).ljust(2,' ')+')'+o2+str(third).ljust(2,' ')+'='
           
                # 将题目写入表格单元格
                cell = table.cell(row,col)
                cell.text = r

        # 保存并打开文档
        document.save('口算题目.docx')
        os.startfile("口算题目.docx")



if __name__ == '__main__':
    root = tk.Tk()
    app = MathQuizGenerator(root)
    root.mainloop()