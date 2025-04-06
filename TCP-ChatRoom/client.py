import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 54321))

alias = input("Choose your alias")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'USERNAME':
                # we are sending our alias to the server
                client.send(alias.encode('ascii'))
            else:
                print(message)
        except:
            print("An error has occurred")
            client.close()
            break