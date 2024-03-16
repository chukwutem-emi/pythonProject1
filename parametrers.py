# The terms parameter and argument can be used for
# the same thing: information that are passed into a
# function. From a function('s perspective: A parameter is
# the variable listed inside the parentheses in the function
# definition. An argument is the value that is sent to the
# function when it is called.)

# nb
# name and salary are the parameters while sam and $9000
# are the argument
def show_employment(name, salary):
    print(f"{name} {salary}")


print("start")
show_employment("sam", "$9000")
print("finish")
