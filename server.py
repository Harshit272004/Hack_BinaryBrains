import socket

# Server configuration
SERVER_IP = '192.168.197.153'  # Replace with the server's IP address
SERVER_PORT = 8888  # Replace with the server's port

# Initialize the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    # Accept incoming connections from clients (in this case, the Exit Node)
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client (in this case, the Exit Node)
    data = client_socket.recv(4096)

    # Process and handle the received data as needed
    print(f"Received data: {data.decode()}")  # Print the received data for demonstration

    # Close the connection to the client (in this case, the Exit Node)
    client_socket.close()
