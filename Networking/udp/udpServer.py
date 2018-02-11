import socket


def main():
    host = '127.0.0.1'
    port = 5000

    # udp socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print('Server Started')

    while True:
        # udp is connectionless, so I only receive the data and address
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Message from: {}'.format(addr))
        print('From connected user: {}'.format(data))
        data = data.upper()
        print('Sending: {}'.format(data))

        # send to the same adrres it came from
        s.sendto(data.encode('utf-8'), addr)

    s.close()


if __name__ == '__main__':
    main()
