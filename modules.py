# A Python module is a file containing Python definitions
# and statements. A module can define functions, classes,
# and variables

# examples:

import converters

print(converters.kg_to_lbs(60))


# example 2:


from converters import kg_to_lbs

kg_to_lbs(100)

print(kg_to_lbs(100))


# example 3

from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)
