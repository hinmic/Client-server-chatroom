#!/usr/bin/env python3

"""
Author: Chi Hin Ng
Date: 12/07/2020
Description: A server side program of a 1 to 1 chat application
"""

import socket
import time
import sys

def client_chat(client_socket):
    print("Type /q to quit")
    print("Enter message to send...")
    print("Waiting for message...")

    msg = ""
    msg_to_send = ""
    msg_length = 0

    while True:
        # Get the length of the incoming message, then receive the message
        msg_length = int(client_socket.recv(100).decode())
        msg = client_socket.recv(msg_length).decode()
        # Check signal of termination
        if msg == "/q":
            break
        print(msg)

        # Send the length of the message, then send the message
        msg_to_send = input(">")
        msg_to_send = msg_to_send.encode()
        client_socket.send(str(len(msg_to_send)).encode())
        client_socket.send(msg_to_send)

def main():
    server_ip = "127.0.0.1"
    server_port = 7777

    # REF: https://www.geeksforgeeks.org/simple-chat-room-using-python/

    # Create a socket that binds to the server address and port number
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((server_ip, server_port))

    # Listen for a connection
    server.listen(1)
    print("Server listening on: localhost on port: ", server_port)

    # Accept a connection requeest
    # Store the socket object and address of the client
    client, client_addr = server.accept()
    print("Connected by ", client_addr)

    # Start a chat
    client_chat(client)

    # Chat ends
    client.close()
    server.close()


if __name__ == "__main__":
    main()
