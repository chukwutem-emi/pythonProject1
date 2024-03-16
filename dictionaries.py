# Dictionary is a built-in Python Data Structure that is mutable.
# It is similar in spirit to List, Set, and Tuples. However, it is
# not indexed by a sequence of numbers but indexed based on keys
# and can be understood as associative arrays. On an abstract level,
# it consists of a key with an associated value. In Python,
# the Dictionary represents the implementation of a hash-table.
# in other words, key value pairs

# exaple
customer = {
    "name": "emi chukwutem",
    "age": 29,
    "is_verified": True
}
print(customer.get("age"))


# example
# we can also update the dictionary

customer = {
        "name": "emi chukwutem",
        "age": 29,
        "is_verified": True
}
customer["name"] = "jacks smith"
print(customer["name"])
print(customer.get("age"))


# example

phone = input("phone: ")
digits_mapping = {
    "0": "zero",
    "1": "one",
    "2": "Two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output = ""
for ch in phone:
   output += digits_mapping.get(ch, "!" ) + " "
print(output)