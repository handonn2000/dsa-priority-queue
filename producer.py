import socket
from model import Message
import pickle

def queue_server():
    host = socket.gethostname()
    port = 5000

    producer_socket = socket.socket()
    producer_socket.connect((host, port))

    while True:
        data = input('->')
        message = pickle.dumps(Message(1, data))
        producer_socket.send(message)
    producer_socket.close()


if __name__ == "__main__":
    queue_server()