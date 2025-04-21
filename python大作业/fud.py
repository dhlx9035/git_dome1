import socket
if __name__ == '__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("",50001))
    s.listen(1)
    conn,address=s.accept()
    data=conn.recv(1024)
    data=data.decode()
    print(data)
    conn.send("kk".encode())
    conn.close()
    s.close()