import socket
from cryptography.fernet import Fernet
import json

# Entry node configuration
ENTRY_NODE_IP = '192.168.67.205'  # Replace with the entry node's IP address
ENTRY_NODE_PORT = 12345  # Replace with the entry node's port
NEXT_NODE_IP = '192.168.67.38'  # Replace with the next node's IP address
NEXT_NODE_PORT = 56789  # Replace with the next node's port

# Initialize the entry node socket
entry_node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
entry_node_socket.bind((ENTRY_NODE_IP, ENTRY_NODE_PORT))
entry_node_socket.listen(5)

print(f"Entry Node listening on {ENTRY_NODE_IP}:{ENTRY_NODE_PORT}")

while True:
    # Accept incoming connections from clients (or previous nodes)
    client_socket, client_address = entry_node_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive JSON data from the client (or previous node)
    data_json = client_socket.recv(4096).decode()
    data = json.loads(data_json)

    # Decrypt the symmetric key with the entry node's private key
    symmetric_key = data['symmetric_key'].encode()

    # Layer 1 Decryption: Decrypt the data with the symmetric key
    encrypted_data = data['encrypted_data'].encode()
    cipher = Fernet(symmetric_key)
    decrypted_data = cipher.decrypt(encrypted_data)

    # Forward the decrypted data to the next node (for illustration purposes)
    # In a real implementation, consider the security requirements and the next node's capabilities
    next_node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    next_node_socket.connect((NEXT_NODE_IP, NEXT_NODE_PORT))
    next_node_socket.sendall(decrypted_data)

    # Close the connection to the next node
    next_node_socket.close()

    # Close the connection to the client (or previous node)
    client_socket.close()
