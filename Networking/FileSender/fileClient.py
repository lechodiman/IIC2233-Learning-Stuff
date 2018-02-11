import socket
import threading
import sys
import pickle


class Client():
    """docstring for Client"""

    def __init__(self, host="localhost", port=4001):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        filename = input('Filename? -> ')
        if filename != 'q':
            self.sock.send(pickle.dumps(filename))
            data = pickle.loads(self.sock.recv(1024))
            if data[:6] == 'EXISTS':
                filesize = int(data[6:])
                message = input('File exists {} Bytes, download? (Y/N)'.format(filesize))
                if message == 'Y':
                    self.sock.send(pickle.dumps('OK'))
                    f = open('new_{}'.format(filename), 'wb')
                    data = self.sock.recv(1024)
                    totalRecv = len(data)
                    f.write(data)
                    while totalRecv < filesize:
                        data = self.sock.recv(1024)
                        totalRecv += len(data)
                        f.write(data)
                    print('Donwload complete')
                    f.close()
            else:
                print('File Does Not Exists')
        self.sock.close()

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print(pickle.loads(data))
            except:
                pass

    def send_msg(self, msg):
        self.sock.send(pickle.dumps(msg))


c = Client()
