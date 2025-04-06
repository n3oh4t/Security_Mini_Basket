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

def write():
    while True:
        message = f'{alias}: {input("")}' # constantly waiting for next input from user.
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

