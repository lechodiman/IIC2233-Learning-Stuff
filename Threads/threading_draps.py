from threading import Thread, Lock
import time

tLock = Lock()


def timer(name, delay, repeat):
    print('Timer: {} started'.format(name))
    tLock.acquire()
    print('{} has acquired the lock'.format(name))
    while repeat > 0:
        time.sleep(delay)
        print('{} : {}'.format(name, time.ctime(time.time())))
        repeat -= 1
    print('{} is releasing the lock'.format(name))
    tLock.release()
    print('Timer: {} Completed'.format(name))


def main():
    t1 = Thread(target=timer, args=('Timer1', 1, 5))
    t2 = Thread(target=timer, args=('Timer2', 2, 5))
    t1.start()
    t2.start()

    print('Main completed')


class AsyncWrite(Thread):
    def __init__(self, text, out):
        super().__init__()
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, 'a')
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print('Finished background file write to {}'.format(self.out))


message = input('Enter a string to store: ')
background = AsyncWrite(message, 'out.txt')
background.start()
print('The program can continue to run while it writes in another thread')
print(100 + 400)

# wait till thread is finished
background.join()
print('Waited until thread was complete')


'''
if __name__ == '__main__':
    main()
'''
