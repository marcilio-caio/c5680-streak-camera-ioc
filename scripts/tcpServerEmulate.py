"""
    Author: Leonardo Rossi Leao
    Date: January 30th, 2024
    Description: Emulate a TCP server to test communication with
    streamdevice EPICS Input/Output controller.
"""

import socket
from _thread import start_new_thread

class TCPServer:

    RECV_BUFFER = 2048

    def __init__(self, host: str, port: int) -> None:

        """
        Constructor method for TCPServer class.

        Args:
            host (str): IP address of the server.
            port (int): Port number of the server.
        """

        self.host = host
        self.port = port

        # Instantiate a socket object and bind it.
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        
        print(f"Server is listening on {self.host}:{self.port}")


    def clientHandler(self, conn: socket.socket) -> None:

        """
        Method to handle with client interactions as requests 
        and responses.

        Args:
            conn (socket.socket): Socket connection object.
        """

        conn.send("Connection established.".encode("utf-8"))

        while True:
            data = conn.recv(self.RECV_BUFFER)
            message = data.decode("utf-8")
            if not data:
                break
            answer = f"Server received: {message}"
            conn.sendall(data)

        conn.close()

    
    def start(self) -> None:

        """
        Method to handle with connections with clients.
        """

        self.server.listen()

        while True:
            conn, addr = self.server.accept()
            print(f"Connected to {addr[0]}:{addr[1]}")
            start_new_thread(self.clientHandler, (conn,))


if __name__ == "__main__":

    HOST = "0.0.0.0"
    PORT = 5555

    server = TCPServer(HOST, PORT)
    server.start()
