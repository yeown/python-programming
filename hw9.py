class Point :
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def get(self):
        return self.x, self.y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.It = Point(x1, y1)
        self.rb = Point(x2, y2)

    def show(self):
        It=self.It.get()
        rb=self.rb.get()
        print(f'좌측 상단 꼭지점이 {It}이고 우측 상단 꼭지점이 {rb}인 사각형입니다.')

    def getWidth(self):
        return self.rb.x-self.It.x

    def getHeight(self):
        return self.rb.y-self.It.y

    def getArea(self):
        return self.getWidth() *self.getHeight()

    def getPerimeter(self):
        return (self.getWidth() + self.getHeight()) *2

r1 = Rectangle(5, 5, 20,10)
a= r1.getArea()
p= r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
