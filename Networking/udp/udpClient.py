import socket


def main():
    host = '127.0.0.1'

    # port has to be different from server
    port = 5001

    server = ('127.0.0.1', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input('-> ')
    while message != 'q':
        s.sendto(message.encode('utf-8'), server)

        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Receive from server: {}'.format(data))

        message = input('-> ')

    s.close()


if __name__ == '__main__':
    main()
