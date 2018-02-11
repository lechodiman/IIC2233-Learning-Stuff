import numpy as np
import time
import sys

'''#l = range(1000)
#print(sys.getsizeof(5) * len(l))
#array = np.arange(1000)
##array.size = len() and array.itemsize is the size of one element
#print(array.size * array.itemsize)'''


SIZE = 1000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python list
start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
print("python list took: ", (time.time() - start) * 1000)

# numpy array
start = time.time()
result = a1 + a2
print("numpy took: ", (time.time() - start) * 1000)

'''#useful methods
#np.std(array)
#np.zeros(dim)
#np.one(dim)
#np.sqrt(array)
#a = np.array([], dtype = np.float64 or complex or int)
#arry.reshape(dim)
#a.flat
#b = a > 4
#a[b]'''

a_1 = np.ones((3, 3))
print(a_1)

a_2 = np.array([1, 2, 3])
