#（2）tkinter 电子时钟
import tkinter as tk
import time

class Clock:
    def __init__(self, master):
        # 初始化窗口
        self.master = master
        #self.master.wm_attributes('-type', '_NET_WM_WINDOW_TYPE_DOCK')
        self.master.overrideredirect(True)  # 不显示标题栏
        self.master.geometry("+0+0")  # 位置在屏幕左上角
        self.master.attributes('-topmost', True)  # 窗口始终在顶层
        self.master.config(bg='black')  # 窗口背景色为黑色           
        self.master.attributes('-alpha', 0.5)  # 窗口透明度初始值为0.5
        
        # 绑定鼠标事件
        self.master.bind("<Button-3>", self.quit)  # 鼠标右键点击退出程序
        self.master.bind("<ButtonPress-1>", self.click)   # 鼠标左键按下，开始移动窗口
        self.master.bind("<ButtonRelease-1>", self.release)  # 鼠标左键松开，停止移动窗口
        self.master.bind("<B1-Motion>", self.drag)          # 鼠标左键拖动，移动窗口

        # 创建标签组件用于显示时间和日期
        self.time_label = tk.Label(master, font=('Digital-7', 50), fg='white', bg='black')
        self.time_label.pack(fill='both', expand=True)

        self.date_label = tk.Label(master, font=('Helvetica', 20), fg='white', bg='black')
        self.date_label.pack(side='bottom', fill='x')

        self.tick()  # 开始时钟

    def tick(self):
        # 更新时间和日期标签内容
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        current_date = time.strftime('%A, %B %d, %Y')
        self.date_label.config(text=current_date)
        # 每秒调用一次tick函数更新时间和日期
        self.master.after(1000, self.tick)

    def click(self, event):
        # 鼠标左键点击时，记录鼠标按下时的坐标,将窗口透明度设置为0.2
        self.x = event.x
        self.y = event.y
        self.master.attributes('-alpha', 0.2)

    def drag(self, event):
        # 计算窗口移动后的新位置，并移动窗口
        self.master.geometry(f'+{event.x_root - self.x}+{event.y_root - self.y}')

    def release(self, event):
        # 鼠标左键释放时，停止移动窗口,将窗口透明度设置为0.5
        self.master.attributes('-alpha', 0.5)

    def quit(self, event):
        # 鼠标右键点击时退出程序
        self.master.quit()
        self.master.destroy()


root = tk.Tk()
clock = Clock(root)
root.mainloop()
