import socket
import paramiko

# SSH connection parameters for the private server
SSH_HOST = 'your_server_hostname_or_ip'
SSH_PORT = 22
SSH_USERNAME = 'your_ssh_username'
SSH_PASSWORD = 'your_ssh_password'

# Report server configuration
REPORT_SERVER_IP = '192.168.67.126'  # Replace with the report server's IP address
REPORT_SERVER_PORT = 5656  # Replace with the report server's port

# Initialize the SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Initialize the report server socket
report_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
report_server_socket.connect((REPORT_SERVER_IP, REPORT_SERVER_PORT))

# Entry node configuration
ENTRY_NODE_IP = '192.168.67.205'  # Replace with the entry node's IP address
ENTRY_NODE_PORT = 12345  # Replace with the entry node's port

# Initialize the entry node socket
entry_node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
entry_node_socket.bind((ENTRY_NODE_IP, ENTRY_NODE_PORT))
entry_node_socket.listen(5)

print(f"Entry Node listening on {ENTRY_NODE_IP}:{ENTRY_NODE_PORT}")

# Function to check for suspicious activity (customize as needed)
def is_suspicious(response):
    # Implement your own logic to detect suspicious activity here
    # For example, check for keywords or patterns in the response
    suspicious_keywords = ["malicious_pattern1", "malicious_pattern2", "suspicious_keyword"]
    
    for keyword in suspicious_keywords:
        if keyword in response.lower():
            return True  # Suspicious activity detected
    
    return False

try:
    # Connect to the private server via SSH
    ssh_client.connect(SSH_HOST, SSH_PORT, SSH_USERNAME, SSH_PASSWORD)

    while True:
        # Accept incoming connections from clients (or previous nodes)
        client_socket, client_address = entry_node_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Receive and process data from the client (or previous node)
        data = client_socket.recv(4096)

        # Forward the data to the private server via SSH
        ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command("your_command_here")

        # Capture and process the response from the server if necessary
        response = ssh_stdout.read()

        # Check for suspicious activity in the response (implement your own logic here)
        if is_suspicious(response):
            # Report the suspicious activity to the report server
            report_message = f"Suspicious activity detected from {client_address}: {response}"
            report_server_socket.sendall(report_message.encode())

        # Close the connection to the client (or previous node)
        client_socket.close()

except paramiko.AuthenticationException:
    print("Authentication failed. Please check your credentials.")
except paramiko.SSHException as e:
    print(f"SSH error: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    # Make sure to close the SSH connection to the private server in all cases
    ssh_client.close()