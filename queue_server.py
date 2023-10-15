import socket
import threading
import pickle
import queue
from model import Message

q = queue.Queue()

def handle_producer(producer):
    while True:
        data = producer.recv(1048576)
        messageEntity = pickle.loads(data)
        if not data:
            break
        print(messageEntity.data)
        q.put(messageEntity.data)

def handle_consumer(consumer):
    while True:
        if not q.empty():
            message = q.get()
            consumer.send(message.encode())

def queue_server():
    host = socket.gethostname()
    producer_port = 5000
    consumer_port = 6000

    producer_socket = socket.socket()
    producer_socket.bind((host, producer_port))
    producer_socket.listen(2)

    consumer_socket = socket.socket()
    consumer_socket.bind((host, consumer_port))
    consumer_socket.listen(2)

    while True:
        producer, p_address = producer_socket.accept()
        print(f"Connection from producer: {p_address}")
        thread = threading.Thread(target=handle_producer, args=(producer,))
        thread.start()

        consumer, c_address = consumer_socket.accept()
        print(f"Connection from consumer: {c_address}")
        thread = threading.Thread(target=handle_consumer, args=(consumer,))
        thread.start()
    conn.close()

if __name__ == "__main__":
    queue_server()