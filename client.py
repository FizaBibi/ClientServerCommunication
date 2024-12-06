import socket
import keyboard
import threading 
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))
client.send("hello world".encode("utf-8"))
data=client.recv(1024)
# Wait for user input to close the connection
# quit_connection=input("Enter q to quit...")
# if quit_connection=='q':
#     client.close()
print("Press q to close connection...")
while True:
    if keyboard.is_pressed('q'):
        client.close()
        print("connection closed successfully")
        break

print("Received from server: ",data.decode("utf-8"))

