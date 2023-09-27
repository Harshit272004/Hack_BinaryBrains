import socket

# Middle node 2 configuration
MIDDLE_NODE2_IP = '192.168.197.58'  # Replace with the middle node 2's IP address
MIDDLE_NODE2_PORT = 67890  # Replace with the middle node 2's port
EXIT_NODE_IP = '192.168.197.8'  # Replace with the exit node's IP address
EXIT_NODE_PORT = 78901  # Replace with the exit node's port

# Initialize the middle node 2 socket
middle_node2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
middle_node2_socket.bind((MIDDLE_NODE2_IP, MIDDLE_NODE2_PORT))
middle_node2_socket.listen(5)

print(f"Middle Node 2 listening on {MIDDLE_NODE2_IP}:{MIDDLE_NODE2_PORT}")

while True:
    # Accept incoming connections from clients (or previous nodes)
    client_socket, client_address = middle_node2_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client (or previous node)
    data = client_socket.recv(4096)

    # Forward the data to the exit node
    exit_node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    exit_node_socket.connect((EXIT_NODE_IP, EXIT_NODE_PORT))
    exit_node_socket.sendall(data)

    # Close the connection to the exit node
    exit_node_socket.close()

    # Close the connection to the client (or previous node)
    client_socket.close()
