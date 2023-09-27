import socket

# Middle node 1 configuration
MIDDLE_NODE1_IP = '192.168.197.38'  # Replace with the middle node 1's IP address
MIDDLE_NODE1_PORT = 56789  # Replace with the middle node 1's port
MIDDLE_NODE2_IP = '192.168.197.58'  # Replace with the middle node 2's IP address
MIDDLE_NODE2_PORT = 67890  # Replace with the middle node 2's port

# Initialize the middle node 1 socket
middle_node1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
middle_node1_socket.bind((MIDDLE_NODE1_IP, MIDDLE_NODE1_PORT))
middle_node1_socket.listen(5)

print(f"Middle Node 1 listening on {MIDDLE_NODE1_IP}:{MIDDLE_NODE1_PORT}")

while True:
    # Accept incoming connections from clients (or previous nodes)
    client_socket, client_address = middle_node1_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client (or previous node)
    data = client_socket.recv(4096)

    # Forward the data to the next middle node (middle node 2)
    next_node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    next_node_socket.connect((MIDDLE_NODE2_IP, MIDDLE_NODE2_PORT))
    next_node_socket.sendall(data)

    # Close the connection to the next middle node
    next_node_socket.close()

    # Close the connection to the client (or previous node)
    client_socket.close()
