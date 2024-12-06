import socket

# Function to handle the sending and receiving of messages for each client
def client_communication(client_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))

    # Continuously listen for user input and send it to the server
    while True:
        message = input(f"Client {client_id} - Enter message to send to server (or 'q' to quit): ")
        
        if message.lower() == 'q':
            print(f"Client {client_id} - Pressed 'q', closing connection.")
            client.close()
            break
        
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        print(f"Client {client_id} - Received from server: {data.decode('utf-8')}")
    
    print(f"Client {client_id} - Connection closed successfully")

# Starting clients sequentially
def start_sequential_clients():
    client_id = 1  # Start from Client 1
    while True:
        start_client = input(f"Do you want to start Client {client_id}? (y/n): ")
        if start_client.lower() == 'y':
            print(f"Starting Client {client_id}...")
            client_communication(client_id)  # Directly call the client communication function
            client_id += 1  # Increment the client ID for the next client
        elif start_client.lower() == 'n':
            print("No more clients will be started.")
            break 

# Call the function to start sequential clients
start_sequential_clients()
