numbers = [5, 2, 1, 7, 4]
numbers.append(5)
print(numbers)

# example2
numbers = [5, 2, 1, 7, 4]
numbers.insert(5, 20)
print(numbers)

# exaple3
numbers = [5, 2, 1, 7, 4]
numbers.remove(7)
print(numbers)

# example4
numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

# example5:
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

# exaple6;

numbers = [5, 2, 1, 7, 4]
print(numbers.index(5))

# or
# > how to find the existence of a number

numbers = [5, 2, 1, 7, 4]
print(2 in numbers)

# exaple7:

numbers = [5, 2, 2, 1, 7, 4]
print(numbers.count(5))

# example8:

numbers = [5, 2, 1, 7, 4]
numbers.sort()
print(numbers)

# example9:
# for decending order

numbers = [5, 2, 1, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)

# example10
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
print(numbers2)

# example
# how to remove duplicate from a list

numbers  = [5, 5, 2, 2, 1, 7, 4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
