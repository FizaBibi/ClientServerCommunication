import socket
import keyboard  # To capture keypresses in real-time
import time

# Function to handle the communication for each client
def client_communication(client_id):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 8080))  # Ensure this matches your server's address and port

        print(f"Connected to Client {client_id}.")
        while True:
            message = input(f"Client {client_id} - Enter message to send to server (or 'q' to quit): ")

            if message.lower() == 'q':  # Disconnect when 'q' is pressed
                print(f"Client {client_id} - Pressed 'q', closing connection.")
                client.close()
                break

            client.send(message.encode("utf-8"))
            data = client.recv(1024)
            print(f"Client {client_id} - Received from server: {data.decode('utf-8')}")

        print(f"Client {client_id} - Connection closed successfully.\n")
    except Exception as e:
        print(f"Client {client_id} - Error: {e}")
        print(f"Client {client_id} - Closing connection.")
        client.close()

# Main function with keyboard functionality
def main_menu():
    print("\n=== Main Menu ===")
    print("Press 'a' to connect to Client 1.")
    print("Press 'b' to connect to Client 2.")
    print("Press 'q' to quit the program.")

    while True:
        if keyboard.is_pressed('a'):  # Connect to Client 1
            print("\nYou pressed 'a' - Connecting to Client 1...")
            time.sleep(0.5)  # To avoid multiple triggers
            client_communication(1)
            print("\n=== Main Menu ===\nPress 'a' to connect to Client 1.\nPress 'b' to connect to Client 2.\nPress 'q' to quit the program.")

        elif keyboard.is_pressed('b'):  # Connect to Client 2
            print("\nYou pressed 'b' - Connecting to Client 2...")
            time.sleep(0.5)  # To avoid multiple triggers
            client_communication(2)
            print("\n=== Main Menu ===\nPress 'a' to connect to Client 1.\nPress 'b' to connect to Client 2.\nPress 'q' to quit the program.")

        elif keyboard.is_pressed('q'):  # Quit the program
            print("\nYou pressed 'q' - Exiting the program. Goodbye!")
            break

        time.sleep(0.1)  # Avoid busy-waiting

# Entry point of the program
if __name__ == "__main__":
    main_menu()
