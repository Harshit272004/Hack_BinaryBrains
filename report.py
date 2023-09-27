import socket
import json

# Report server configuration
REPORT_SERVER_IP = '192.168.197.213'  # Replace with the report server's IP address
REPORT_SERVER_PORT = 9999  # Replace with the report server's port

# Initialize the report server socket
report_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
report_server_socket.bind((REPORT_SERVER_IP, REPORT_SERVER_PORT))
report_server_socket.listen(5)

print(f"Report Server listening on {REPORT_SERVER_IP}:{REPORT_SERVER_PORT}")

while True:
    # Accept incoming connections from the bot
    bot_socket, bot_address = report_server_socket.accept()
    print(f"Accepted connection from {bot_address}")

    # Receive JSON data from the bot
    data_json = bot_socket.recv(4096).decode()
    data = json.loads(data_json)

    # Check if the data is marked as malicious by the bot
    if data.get("is_malicious"):
        # Log the client's IP address (without compromising anonymity)
        client_ip = data.get("client_ip")
        print(f"Malicious activity detected from client: {client_ip}")

        # Log additional information or take appropriate actions as needed

    # Close the connection to the bot
    bot_socket.close()
