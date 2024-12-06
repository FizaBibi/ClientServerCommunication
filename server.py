import socket
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1",8080))
server.listen(5)
while True:
    conn,addr=server.accept()
    from_client=""
    while True:
        data=conn.recv(1024)
        if not data:
            break
        from_client+=data.decode()
        
        conn.send(data)
    conn.close()
    print("Client disconnected:",from_client)


