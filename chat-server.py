import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Replace 'hostname_or_ip' with the actual hostname or IP address of Mac 1
host = 'hostname_or_ip'

# Set the port for communication
port = 12345

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")
conn, addr = server_socket.accept()
print("Connected by", addr)

while True:
    # Receive data from the client
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Received message: {data}")
    response = input("Your response: ")
    conn.send(response.encode())

conn.close()
