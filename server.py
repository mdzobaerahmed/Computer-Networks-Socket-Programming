import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()


clients = {}
print("Server Started...")
print("Waiting for clients...")

def send_all(message, sender):
    for user in clients:
        if user != sender:
            try:
                clients[user].send(message.encode())
            except:
                pass


def send_private(receiver, message):
    if receiver in clients:
        clients[receiver].send(message.encode())

    else:
        print("User not found")


def send_group(users, message):
    for user in users:
        user = user.strip()
        if user in clients:
            clients[user].send(message.encode())



def client_handler(client):
    username = client.recv(1024).decode()
    clients[username] = client
    print(username, "connected")
    send_all(
        username + " joined the chat",
        username
    )


    while True:
        try:
            message = client.recv(1024).decode()
            if message == "":
                break

            if message.startswith("/all"):
                text = message[5:]
                send_all(
                    username + ": " + text,
                    username
                )

            elif message.startswith("/pm"):
                data = message.split(" ",2)
                receiver = data[1]
                text = data[2]
                send_private(
                    receiver,
                    "[Private] "+username+": "+text
                )

            elif message.startswith("/group"):
                data = message.split(" ",2)
                users = data[1].split(",")
                text = data[2]
                send_group(
                    users,
                    "[Group] "+username+": "+text
                )

            elif message == "/users":
                user_list = str(list(clients.keys()))
                client.send(
                    user_list.encode()
                )

        except:
            print(username,"left")
            del clients[username]
            break


while True:
    client, address = server.accept()
    print("New connection:", address)
    thread = threading.Thread(
        target=client_handler,
        args=(client,)
    )
    thread.start()