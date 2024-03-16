# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration
# of the "outer loop":
# it means adding one loop into another loop

# example 1:

for x in range(4):
    print(x)

# example 2:

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# example 3:

numbers = [8, 2, 2, 5, 2, 2, 8]
number2 = [8, 2, 2, 5, 2, 2, 8]
sum = numbers + number2
for x_count in sum:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)

