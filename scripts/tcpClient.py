"""
    Author: Leonardo Rossi Leao
    Date: January 30th, 2024
    Description: Emulate a TCP client to test communication with
    TCP server emulator.
"""

import socket


class TCPClient:


    def __init__(self, host: str, port: int) -> None:

        """
        Constructor method for TCPClient class.

        Args:
            host (str): IP address of the server.
            port (int): Port number of the server.
        """

        self.host = host
        self.port = port
        self.is_connected = False

        # Instantiate a socket object and connect it to the server.
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.host, self.port))
            self.is_connected = True
            print(f"Connected to {self.host}:{self.port}")
        except ConnectionRefusedError:
            print("Connection refused. Check if the server is running.")

    
    def send(self, message: str) -> str:

        """
        Method to send a message to the server.

        Args:
            message (str): Message to be sent to the server.

        Returns:
            str: Response from the server.
        """

        self.client.sendall(message.encode("utf-8"))
        response = self.client.recv(2048)
        return response.decode("utf-8")
    

    def close(self) -> None:

        """
        Method to close the connection with the server.
        """

        self.client.close()


if __name__ == "__main__":
    client = TCPClient("localhost", 55555)
    if client.is_connected:
        message = "Hello, server!"
        response = client.send(message)
        print(response)
        client.close()
