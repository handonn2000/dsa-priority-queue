# ConsumerServer.py
import socket

def consumer_server():
    host = socket.gethostname()
    port = 6000
    consumer_socket = socket.socket()
    consumer_socket.connect((host, port))
    print("Start Consume")

    while True:
        data = consumer_socket.recv(1048576).decode()

        print('Received from server: ' + data)
    consumer_socket.close()

    
if __name__ == "__main__":
    consumer_server()
