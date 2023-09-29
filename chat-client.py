import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Replace 'hostname_or_ip' with the actual hostname or IP address of Mac 1
host = 'hostname_or_ip'

# Set the port for communication
port = 12345

# Connect to the server
client_socket.connect((host, port))

while True:
    message = input("Your message: ")
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Received response: {response}")

client_socket.close()
