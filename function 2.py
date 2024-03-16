def say_hello():
    print("hello!")


print("start")
say_hello()
print("finish")


# example 2:

def say_hello(name):
    print(f"hello! {name}")


print("start")
say_hello("john")
print("finish")


# example 3:

def greet_user(name, age):
    print(f"hello! {name}, you are {age} years old")
    pass


print("start")
greet_user("john", "29")
print("finish")
