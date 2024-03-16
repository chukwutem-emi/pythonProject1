# Write a function called calculation() that takes in
# 2 integers, a and b, and a sign (which will be a
# string -- either "+" or "-"). If the sign is "+" return the sum
# of a and b. Otherwise, if the sign is "-", return a - b.

# answer:

def calculation(a,b, sign):
    while sign == "+" or "-":
        if sign == "+":
            return a + b
        else:
            return a - b


print("start")
print(calculation(3, 5, "+"))
print("finish")



# Create a function called showEmployee() such that it should
# accept an employee name and salary and print both of them out.

# answer:

def show_employment(name,salary):
    print(f"{name} {salary}")


print("start")
show_employment("sam","$9000" )
print("finish")


# 1. Create an outer function that will accept two parameters
# a and b
#
# 2. Inside that function, create another inner function that
# will calculate a+b
#
# 3. Then add 8 to the number in the original outer function.


# answer:
def outerFun(a, b):
    def innerFun(a, b):
        return a+b
    add = innerFun(a, b)
    return add+8

result = outerFun(5, 10)
print(result)



# Write a function that takes in a string and determines whether
# the string is a Palindrome or not (reads the same forwards
# and backward). The function should return a boolean value
# (True, False) depending on whether the string is a Palindrome.
#
# Examples of Palindromes: Racecar, Kayak

# answer:

def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True


print(isPalindrome('aza'))


