import socket


def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()

    # bind to a port
    s.bind((host, port))

    # start listening for connections
    s.listen(1)

    c, addr = s.accept()
    print('Connection from: {}'.format(addr))

    while True:
        # recieve bytes buffer = 1024
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print('From connected user: {}'.format(data))
        data = str(data).upper()
        print('Sending: {}'.format(data))

        # send
        c.send(data.encode('utf-8'))
    c.close()


if __name__ == '__main__':
    main()
