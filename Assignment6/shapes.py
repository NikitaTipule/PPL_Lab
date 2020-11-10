import turtle

s = turtle.getscreen()
t = turtle.Turtle()


class shape:
    def __init__(self, sides = 0, length = 0):
        self.sides = sides
        self.length = length

class polygon(shape):
    def info(self):
        print("In geometry , a polygon can be defined as a flat or plane , two dimentional with straight sides")

class square(polygon):
    def show(self):
        for i in range(4):
           t.fd(self.length)
           t.rt(90)


class pentagon(polygon):
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) 

class hexagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(60)

class octagon(polygon):
    def show(self):
        for i in range(8):
           t.forward(self.length) 
           t.right(45)

class triangle(polygon):
    def show(self):
        t.forward(self.length) 
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)

t.circle(100)
hex1 = hexagon(6, 100)
hex1.info()
hex1.show()


octa = octagon(12,100)
octa.info()
octa.show()

squ = square(4,100)
squ.info()
squ.show()
tri = triangle(3,100)
tri.info()
tri.show()
penta = pentagon(5,100)
penta.info()
penta.show()













