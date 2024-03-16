# how to handle errors in python


try:
    age = int(input("age: "))
    print(age)
except ValueError:
    print("invalid value")
pass

# example 2:
try:
    age = int(input("age: "))
    income = 800000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print("age cannot be 0.")
except ValueError:
    print("invalid value")
