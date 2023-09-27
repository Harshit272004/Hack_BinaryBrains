import socket
from cryptography.fernet import Fernet
import json

# Generate a random symmetric key for encryption
symmetric_key = Fernet.generate_key()
cipher = Fernet(symmetric_key)

# Your secret message
message = b"This is a secret message."

# Encrypt the message with the symmetric key
encrypted_data = cipher.encrypt(message)

# Prepare the data to be sent
data_to_send = {
    "encrypted_data": encrypted_data.decode(),
    "symmetric_key": symmetric_key.decode()
}

# Convert to JSON
data_json = json.dumps(data_to_send)

# Create a socket and connect to the entry node
entry_node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
entry_node_socket.connect(('192.168.197.126', 12345))

# Send the data to the entry node
entry_node_socket.sendall(data_json.encode())

# Close the connection to the entry node
entry_node_socket.close()
