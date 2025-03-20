# Network communication implementation using TCP/IP sockets
# Provides server and client classes for component communication
# Handles message serialization and async communication

import socket
import json
import threading
from .utils import setup_logging

class TCPServer:
    def __init__(self, host, port, message_handler):
        self.host = host
        self.port = port
        self.message_handler = message_handler
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        
        while True:
            conn, addr = self.socket.accept()
            thread = threading.Thread(
                target=self._handle_client,
                args=(conn, addr)
            )
            thread.start()
            
    def _handle_client(self, conn, addr):
        while True:
            data = conn.recv(4096)
            if not data:
                break
            message = json.loads(data.decode())
            self.message_handler(message, addr)

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self):
        self.socket.connect((self.host, self.port))
        
    def send(self, message):
        self.socket.sendall(json.dumps(message).encode()) 