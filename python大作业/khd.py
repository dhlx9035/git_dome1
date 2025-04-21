import socket
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1",50001))
    s.sendall("ok".encode())
    data=s.recv(1024)
    print(data)
    s.close()