import threading
import time
import random
import queue as Queue


class Producer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.food = ['ham', 'soup', 'salad']
        self.next_time = 0

    def run(self):
        global q
        while time.clock() < 10:
            if self.next_time < time.clock():
                f = self.food[random.randrange(len(self.food))]
                q.put(f)
                print('Adding ' + f)
                self.next_time += random.random()


class Consumer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.next_time = 0

    def run(self):
        global q
        while time.clock() < 10:
            if self.next_time < time.clock() and \
                    not q.empty():
                f = q.get()
                print('Removing ' + f)
                self.next_time += random.random() * 2


if __name__ == '__main__':
    q = Queue.Queue(20)
    p = Producer()
    c = Consumer()
    # c_t will consume after 5 secs
    c_t = threading.Timer(5, c.run, args=())
    p.start()
    # c_t.start()
    c.start()
    # if not p.isAlive():
    #     print("Thread has finished")
    # else:
    #     print('Thread has not finished')

    # print("This should be printed at the end")
    # c.join(1)
    # print('p alive?: {}'.format(p.isAlive()))
    # c.join()
