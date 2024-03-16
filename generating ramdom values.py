import random

for i in range(3):
    print(random.random())

# example2:
import random

for i in range(3):
    print(random.randint(10, 20))

# example3:


members = ["john", "mary", "bob", "mosh"]
leader = random.choice(members)
print(leader)

# exercise:
import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
