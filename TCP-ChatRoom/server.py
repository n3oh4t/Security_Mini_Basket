import threading
import socket

host = '127.0.0.1' #localhost = hosting on our local machine
port = 98765 # random port (un-reserved port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.socket().setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #To re-use the same port after a connection gets disconnected.

server.bind((host, port)) # binding host and port

server.listen() #listen-mode => server starts listening for connections
