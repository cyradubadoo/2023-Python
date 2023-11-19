import math

class Circle:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

# 测试方法
my_circle = Circle(3, 2, 10, "red")
print(f"圆的坐标是： ({my_circle.x},{my_circle.y})")
print("圆的半径是：", my_circle.r)
print("圆的颜色是：", my_circle.color)
print("圆的周长是：", my_circle.perimeter())
print("圆的面积是：", my_circle.area())
