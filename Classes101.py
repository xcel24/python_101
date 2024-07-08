class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
    def draw(self):
        print("draw")


p = Point(10,20)
print(f"Value of x is {p.x} and y is {p.y}")


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi my name is {self.name}")


person = Person("Prateek")

person.talk()