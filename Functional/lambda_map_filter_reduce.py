# Lambda

my_sum = lambda x, y: x + y
print(my_sum(2, 3))

# Map: applies function to a list and it returns it


def square(list_1):
    list_2 = []
    for num in list_1:
        list_2.append(num ** 2)
    return list_2


n = [4, 3]
print(square([4, 3]))

print(list(map(lambda x: x**2, n)))

print([num**2 for num in n])

gen = (num**2 for num in n)
print(list(gen))

for i in gen:
    print(next(i))

# Filter: it applies a condition to a list, and it returns
# the ones that passes it

n = [4, 3, 2, 1]
print(list(filter(lambda x: x > 2, n)))

print([num for num in n if num > 2])

# Reduce: it applies same operation to items of a sequence
# returns an item, not a list

from functools import reduce

n = [4, 3, 2, 1]
print(reduce(lambda x, y: x * y, n))
