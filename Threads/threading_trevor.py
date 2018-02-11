import threading
import random
import time


def Splitter(words):
    mylist = words.split()
    new_list = []
    while mylist:
        new_list.append(mylist.pop(random.randrange(0, len(mylist))))
    print(' '.join(new_list))


if __name__ == '__main__':
    sentence = 'I am a handsome beast. Word.'
    NUM_THREADS = 5
    thread_list = []

    print('STARTING..\n')
    for i in range(NUM_THREADS):
        t = threading.Thread(target=Splitter, args=(sentence, ))
        t.start()
        thread_list.append(t)

    print('\nThread Count: {}'.format(threading.activeCount()))
    print('EXITING...\n')
    # for t in thread_list:
    #     t.join()

    print('It took :{}'.format(time.clock()))
