# the  first charracter should be in capital letter e.g
# Point
#
# we dont use underscore but capitalize the first letter
# of the type.
# nb: we use class to define type

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
point1.move()