x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a', "b", "c", "d"]

# for a, b, c in zip(x, y, z):
#     print(a, b, c)

# print(list(zip(x, y, z)))
# print(dict(zip(x, y)))
#
# [print(a, b, c) for a, b, c in zip(x, y, z)]

# [print(a, b) for a, b in zip(x, y)]

# for x, y in zip(x, y):
#     print(x, y)

# x is overwritten after the for loop
# In list coprehension it does not store the values
# print(x)

# GENERATORS (again) ##################


# def simple_gen():
#     yield 'oh'
#     yield 'hello'
#     yield 'there'


# for i in simple_gen():
#     print(i)

CORRECT_COMBO = (3, 6, 1)

# found_combo = False
# for c1 in range(10):
#     if found_combo:
#         break
#     for c2 in range(10):
#         if found_combo:
#             break
#         for c3 in range(10):
#             if (c1, c2, c3) == CORRECT_COMBO:
#                 print('Found the combo: {}'.format((c1, c2, c3)))
#                 found_combo = True
#                 break
#             print(c1, c2, c3)


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)


for (c1, c2, c3) in combo_gen():
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo: {}'.format((c1, c2, c3)))
        break
    print(c1, c2, c3)
