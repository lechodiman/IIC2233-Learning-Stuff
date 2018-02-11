import socket
import time

host = '127.0.0.1'
port = 5000

clients = list()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

# it will not block if there is no data
s.setblocking(0)

quitting = False
print('Server Started')

while not quitting:
    # it throws an error if there is no data to receive
    try:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        if 'Quit' in data:
            quitting = True
        if addr not in clients:
            clients.append(addr)

        print('{}, {}: {}'.format(time.ctime(time.time()), addr, data))

        # send message to all clients currently talking in the chat
        for client in clients:
            s.sendto(data.encode('utf-8'), client)
    except BlockingIOError:
        pass

s.close()
