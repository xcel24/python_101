class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("woof woof ...")


class Cat(Mammal):
    def meow(self):
        print("meow..")


cat = Cat()
cat.walk()
cat.meow()

dog = Dog()
dog.walk()
dog.bark()