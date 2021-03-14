#!/usr/bin/env python3

"""
Author: Chi Hin Ng
Date: 12/07/2020
Description: A client side program of a 1 to 1 chat application
"""

import socket
import time
import sys

def server_chat(client_socket):
    print("Type /q to quit")
    print("Enter message to send...")

    msg = ""
    msg_to_send = ""
    msg_length = 0

    while True:
        # Send the length of the message, then send the message
        msg_to_send = input(">")
        msg_to_send_byte = msg_to_send.encode()
        client_socket.send(str(len(msg_to_send_byte)).encode())
        client_socket.send(msg_to_send_byte)
        # Terminate the program if a termination signal is sent
        if msg_to_send == "/q":
            break

        # Get the length of the incoming message, then receive the message
        msg_length = int(client_socket.recv(100).decode())
        msg = client_socket.recv(msg_length).decode()
        print(msg)


def main():
    server_ip = "127.0.0.1"
    server_port = 7777

    # REF: https://www.geeksforgeeks.org/simple-chat-room-using-python/

    # Create a socket that binds to the client address and port number
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    print("Connected to: localhost on port: ", server_port)

    # Start a chat
    server_chat(client)

    # Chat ends
    client.close()


if __name__ == "__main__":
    main()
