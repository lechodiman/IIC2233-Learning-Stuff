from threading import Thread
import time


class MyTimer():

    def __init__(self, target, args):
        self.oneShot = False
        self.timeout = 1000
        self.target = target
        self.args = args

    def setOneShot(self, b):
        self.oneShot = b

    def setTimeOut(self, timeout):
        self.timeout = timeout

    def start(self):
        if self.oneShot:
            self.target(*self.args)
        else:
            while True:
                self.target(*self.args)
                time.sleep(self.timeout / 1000)
