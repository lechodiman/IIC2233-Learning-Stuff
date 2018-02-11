import time
import threading

lock = threading.Lock()


def calc_square(numbers):
    print('calculate square numbers')
    for n in numbers:
        time.sleep(0.2)
        print('square: {}'.format(n * n))


def calc_cube(numbers):
    print('calculate cube numbers')
    for n in numbers:
        time.sleep(0.2)
        print('cube: {}'.format(n * n * n))


arr = [2, 3, 8, 9]

start = time.time()

for i in range(50):
    t = threading.Thread(target=calc_cube, args=(arr, ))
    t.start()

# t1 = threading.Thread(target=calc_square, args=(arr, ))
# t2 = threading.Thread(target=calc_cube, args=(arr, ))
#
# t1.start()
# t2.start()

print("hi i am between the start and join")

# t1.join()
# t2.join()

print("i am after the join")

print('done in: ', time.time() - start)
print('Hah... I am done with all my work now')
