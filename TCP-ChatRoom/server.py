import threading
import socket

host = '127.0.0.1'  # localhost = hosting on our local machine
port = 98765  # random port (un-reserved port)

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


def handle(client):
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