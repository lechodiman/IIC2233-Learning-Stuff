import socket
import threading
import os
import sys
import pickle


class Server():

    def __init__(self, host='localhost', port=4001):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)

        accept_conn = threading.Thread(target=self.accept_conn)
        accept_conn.setDaemon(True)
        accept_conn.start()

        print('Server started')

        while True:
            msg = input('->')
            if msg == 'salir':
                self.sock.close()
                sys.exit()
            else:
                pass

    def retr_file(self, name, conn):
        print('Retr_file started')
        filename = pickle.loads(conn.recv(1024))
        if os.path.isfile(filename):
            msg = 'EXISTS {}'.format(os.path.getsize(filename))
            conn.send(pickle.dumps(msg))
            user_response = pickle.loads(conn.recv(1024))
            if user_response[:2] == 'OK':
                with open(filename, 'rb') as f:
                    bytes_to_send = f.read(1024)
                    conn.send(bytes_to_send)
                    while bytes_to_send != "":
                        bytes_to_send = f.read(1024)
                        conn.send(bytes_to_send)
        else:
            conn.send('ERR ')

        conn.close()

    def accept_conn(self):
        print("Accept conn started")
        while True:
            try:
                conn, addr = self.sock.accept()
                # conn.setblocking(False)
                t = threading.Thread(target=self.retr_file, args=('retr_thread', conn))
                t.setDaemon(True)
                t.start()
            except:
                pass


server = Server()
