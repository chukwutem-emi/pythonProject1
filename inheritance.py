# The method of inheriting the properties of parent class
# into a child class is known as inheritance. It is an OOP concept

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
     pass

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.walk()


# example 2

class Mammal:
    def bark(self):
        print("bark")


class Dog(Mammal):
     pass

class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

cat1 = Cat()
cat1.be_annoying()
dog1 = Dog()
dog1.bark()