import socket

# Exit node configuration
EXIT_NODE_IP = '192.168.197.8'  # Replace with the exit node's IP address
EXIT_NODE_PORT = 78901  # Replace with the exit node's port
SERVER_IP = '192.168.197.213'  # Replace with the server's IP address
SERVER_PORT = 8888  # Replace with the server's port

# Initialize the exit node socket
exit_node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exit_node_socket.bind((EXIT_NODE_IP, EXIT_NODE_PORT))
exit_node_socket.listen(5)

print(f"Exit Node listening on {EXIT_NODE_IP}:{EXIT_NODE_PORT}")

while True:
    # Accept incoming connections from the last middle node
    middle_node_socket, middle_node_address = exit_node_socket.accept()
    print(f"Accepted connection from {middle_node_address}")

    # Receive data from the last middle node
    data = middle_node_socket.recv(4096)

    # Perform decryption and processing here (if needed)
    # For example, if you want to decrypt data encrypted with Fernet:
    # symmetric_key_layer2 = Fernet.generate_key()
    # cipher_layer2 = Fernet(symmetric_key_layer2)
    # decrypted_data_layer2 = cipher_layer2.decrypt(data)

    # Forward the data to the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((SERVER_IP, SERVER_PORT))
    server_socket.sendall(data)

    # Close the connection to the server
    server_socket.close()

    # Close the connection to the last middle node
    middle_node_socket.close()
