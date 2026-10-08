import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")
client.send(username.encode())

print("""
--- Chat Commands ---
/all <message>
/pm <username> <message>
/group <user1,user2> <message>
/users
/exit
""")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("\nDisconnected from server.")
            client.close()
            break

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    try:
        msg = input()

        if msg == '/exit':
            print("Exiting chat...")
            client.close()
            break
            
        client.send(msg.encode())
    except:
        break