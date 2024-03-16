# A constructor is a unique function that gets called
# automatically when an object of a class is created.
# The main purpose of a constructor is to initialize or assign
# values to the data members of that class. It cannot return any
# value other than none.


# example:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)


# define a new type: person and this person will have
# object -- name attribute as well as a talk meta

class Person:
     def __init__(self, name):
         self.name = name



     def talk(self):
        print(f"hi!, i am {self.name}")


john = Person("john smith")
john.talk()

bob = Person("bob smith")
bob.talk()



