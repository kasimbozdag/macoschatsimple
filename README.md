# Simple Chat Program (Python)

This is a basic chat program implemented in Python using client and server scripts. The program allows two computers on the same network to exchange text messages.

## Instructions

### Prerequisites

- Python installed on both computers (Python 3.x recommended).

### Server Setup (Mac 1)

1. Open the `chat-server.py` script on the first computer (Mac 1).

2. Modify the `host` variable to specify the IP address or hostname of Mac 1. Ensure it's reachable by the client computer (Mac 2).

3. Set the `port` to a specific port number (e.g., 12345).

4. Run the `chat-server.py` script. It will wait for incoming connections.

### Client Setup (Mac 2)

1. Open the `chat-client.py` script on the second computer (Mac 2).

2. Modify the `host` variable to specify the IP address or hostname of Mac 1 (the same one used in the server script).

3. Set the `port` to the same port number used in the server script (e.g., 12345).

4. Run the `chat-client.py` script. It will connect to the server (Mac 1).

5. Enter your messages in the terminal. They will be sent to the server and displayed there.

6. You will receive responses from the server, which you can view in the terminal on Mac 2.

### Finding the Server's IP Address

To determine the IP address of the server computer (Mac 1), you can use the `ipconfig` command on macOS. Follow these steps:

1. Open Terminal on Mac 1 (the server computer).

2. Use the following command to display the IP address associated with your network connection. If you are using Wi-Fi, use "en0"; if you are using Ethernet, use "en1":

   For Wi-Fi (en0):

   ```bash
   ipconfig getifaddr en0
   ```

   For Ethernet (en1):

   ```bash
   ipconfig getifaddr en1
   ```

3. The command will output the IP address, which you can use as the `host` variable in the `chat-client.py` script on other computers to connect to the server.

Make sure to replace the `host` variable in the `chat-client.py` script on other computers with the actual IP address obtained from this command to establish a connection to the server.

### Chatting

- To start a chat, run the server script on Mac 1 first and then the client script on Mac 2.

- Messages are exchanged between the client and server. Type a message in the client script, and it will be sent to the server. The server can then send responses back to the client.

- The chat is basic and text-based. Each message sent by a client is displayed on the server with a "Received message:" prefix, and the server's response is displayed on the client with a "Received response:" prefix.

- To exit the chat, you can press `Ctrl+C` in the terminal where the scripts are running to stop the server and client scripts.

## Notes

- This is a simple example for educational purposes. For a real-world chat application, consider security, error handling, and scalability.

- You may need to adjust your firewall or security settings to allow communication on the specified port.

- Make sure both computers are on the same local network for the chat to work properly.
