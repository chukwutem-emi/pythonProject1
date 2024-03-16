# A for loop is used for iterating over a sequence (that
# is either a list, a tuple, a dictionary, a set, or a string).


for item in "python":
    print(item)

# example2:

for item in ["stephen", "chukwutem", "success", "peace"]:
    print(item)

# example3:

for item in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(item)

# example4:
# the parenthesis changed

for item in range(10):
    print(item)
pass

# example 5:
for item in range(10, 5, 2):
    print(item)

# question:
# write a program to calculate the total cost of item in a shopping mall

prices = [10, 20, 30, 40]
total = 0
for price in prices:
    total += price
print(f"total:{total}")
