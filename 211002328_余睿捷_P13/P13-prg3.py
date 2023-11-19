class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def eq(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'

# 创建一个坐标为(1，8)的对象
coordinate1 = Coordinate(1, 8)

# 用str()方法和repr()方法分别显示该对象
print(str(coordinate1))  # <1,8>
print(repr(coordinate1))  # Coordinate(1,8)

# 再创建一个坐标为(1，8)的对象，并判断这两个对象是否相等
coordinate2 = Coordinate(1, 8)
print(coordinate1.eq(coordinate2))  # True
