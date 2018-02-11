import time
import threading


class Value:
    def __init__(self, value):
        self.value = value


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            balance.value -= 1


balance = Value(200)
lock = threading.Lock()
d = threading.Thread(target=deposit, args=(balance, lock))
w = threading.Thread(target=withdraw, args=(balance, lock))
d.start()
w.start()

d.join()
w.join()
print('Balance: {}'.format(balance.value))
