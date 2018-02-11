import socket
from threading import Thread

PORT = 2500
HOST = '127.0.0.1'


class Server:

    def __init__(self):
        '''host: str '''
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind socket to a port
        self.s.bind((HOST, PORT))
        self.s.listen(2)

        # initialize list of clients
        self.connections = list()
        self.s.setblocking(False)

        print('Server Started')

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for c in self.connections:
                c.send(data)
            if not data:
                print('{} : {} disconnected to Server'.format(c, a))
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while input("") != 'salir':
            try:
                c, a = self.s.accept()
                c.setblocking(False)
                cThread = Thread(target=self.handler, args=(c, a))
                cThread.setDaemon(True)
                cThread.start()
                self.connections.append(c)
                print('{} : {} connected to Server'.format(c, a))
            except:
                pass


server = Server()
server.run()
