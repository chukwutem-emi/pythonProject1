# Write a while loop that prints out the
# following multiples of 2:
#
# 2 4 6 8 10 12 14 16 18 20
# answer:
i = 0

while i < 20:
    i += 2
    print(i)
#
# Write a for loop that prints out the following
# multiples of 2:
#
# 2 4 6 8 10 12 14 16 18 20

# answer:
for i in range(2, 21, 2):
    print(i)

# Write a program that inputs a number n and prints the
# sum of all of the numbers from 1 to n:

# answer:

n = int(input("Input a value for n: "))
summation = 0

for i in range(1, n + 1):
    summation = summation + i

print(summation)




# Write a program that creates a list with the following integers:
# 3, 5, 9, 3, 2, 9, 10. The program should iterate through the
# values in the list and print out each of the integers on
# separate lines

# answers:
numbers = [3, 5, 9, 3, 2, 9, 10]
for col in numbers:
    print(col)



# Write a program that creates a tuple with the following strings:
# "one", "two", "three", "four", "five". The program should print
# out the length of each string in the tuple on different lines

# answers:

string = ["one", "two", "three", "four", "five"]
for col in string:
    print(len(col))