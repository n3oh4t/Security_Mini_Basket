import random
import threading
import socket

colors = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "purple": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_purple": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
}

reset = "\033[0m"

host = '127.0.0.1'  # localhost = hosting on our local machine
port = 54321  # random port (un-reserved port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.socket().setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                           1)  # To re-use the same port after a connection gets disconnected.

server.bind((host, port))  # binding host and port

server.listen()  # listen-mode => server starts listening for connections

clients = []  # clients connecting to the chatroom
aliases = []  # usernames when in chat

def broadcast_message(message):  # broadcasting message to all people in chatroom.
    for client in clients:
        client.send(message)


def handle_connections(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast_message(message)  # broadcast message to all people
        except:
            # cut connection to client
            index = clients.index(client)
            clients.remove(client)  # removing client from the list.
            client.close()
            alias = aliases[index]
            aliases.remove(alias)  # removing the username as well from the list
            broadcast_message(f"{alias} has left the chat!".encode('ascii')) # broadcast to all clients that the particular client has left.
            break

def receive_new_connections(): #receive client connection
    while True:
        client, ip_address_port_num = server.accept()
        print(f"Yahoo!! Client connected from IP Address = {ip_address_port_num[0]} and port number = {ip_address_port_num[1]}")

        client.send("USERNAME".encode('ascii'))
        alias = client.recv(1024).decode('ascii') # decoding the response received.

        aliases.append(alias)
        clients.append(client)

        random_color_key = random.choice(list(colors.keys()))

        # Get the ANSI code for the randomly selected color
        random_color_code = colors[random_color_key]

        print(f"Alias of the client is {random_color_code}{alias}{reset}")
        broadcast_message(f"{alias} has joined the chat!".encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle_connections, args=(client,))
        thread.start()

print("Server is listening")
receive_new_connections()