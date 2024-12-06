import socket
import threading
import uuid
import logging

# Configure logging to see what is happening
logging.basicConfig(level=logging.INFO)

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(5)
logging.info("Server is listening on 127.0.0.1:8080")

# Function to handle client communication
def handle_client(client_socket):
    client_id = str(uuid.uuid4())  # Generate a unique client ID
    logging.info(f"New connection from {client_socket.getpeername()}, assigned client ID: {client_id}")
    
    try:
        while True:
            data = client_socket.recv(1024)  # Receive data from client
            if not data:  # If no data is received, client has closed connection
                break
            
            logging.info(f"Received from {client_id}: {data.decode('utf-8')}")
            client_socket.send(data)  # Echo the data back to client
            
    except ConnectionResetError as e:
        logging.error(f"Connection reset error with client {client_id}: {e}")
    finally:
        client_socket.close()
        logging.info(f"Connection with client {client_id} closed")

# Accept clients and handle them
def accept_clients():
    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# Start accepting clients
accept_clients()
