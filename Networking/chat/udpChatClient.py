import socket
from threading import Thread

PORT = 2500
HOST = '127.0.0.1'


class Client:

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))

        iThread = Thread(target=self.send_msg)
        iThread.setDaemon(True)
        iThread.start()

        while True:
            data = self.s.recv(1024)
            if not data:
                break
            print(data)

    def send_msg(self):
        while True:
            self.s.send(bytes(input("-> "), 'utf-8'))


c = Client()
