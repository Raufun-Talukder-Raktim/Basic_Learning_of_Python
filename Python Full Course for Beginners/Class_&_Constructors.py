class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw ")


#point1 = Point()
#point1.x = 10
#point1.y = 20
#print(point1.x)
#point1.draw()

#point2 = Point()
#point2. x = 1

point = Point(10,20)
print(point.x)

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("john Smith")
#print(john.name)
john.talk()

raktim = Person("Raktim Talukder Raktim")
raktim.talk()
