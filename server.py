import socket
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Global variables to track active clients
active_clients = 0
lock = threading.Lock()

# Function to handle client connections
def handle_client(client_socket, client_address, server_socket):
    global active_clients
    with lock:
        active_clients += 1  # Increment active client count

    logging.info(f"Accepted connection from {client_address}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break  # Client disconnected
            
            message = data.decode('utf-8')
            logging.info(f"Received message: {message}")
            client_socket.send(f"Echo: {message}".encode("utf-8"))
    except Exception as e:
        logging.error(f"Error with client {client_address}: {e}")
    finally:
        logging.info(f"Closing connection from {client_address}")
        client_socket.close()
        
        with lock:
            active_clients -= 1  # Decrement active client count
            if active_clients == 0:  # If no active clients remain
                logging.info("All clients disconnected. Stopping server.")
                server_socket.close()  # Stop the server from listening

# Function to start the server and listen for connections
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    logging.info("Server is listening on 127.0.0.1:8080")

    try:
        while True:
            client_socket, client_address = server.accept()
            # Spawn a thread to handle each client
            threading.Thread(target=handle_client, args=(client_socket, client_address, server)).start()
    except Exception as e:
        logging.error(f"Server error: {e}")
    finally:
        logging.info("Server shutting down.")
        server.close()

# Main function
if __name__ == "__main__":
    start_server()
