import socket
import asyncio
import logging


def cHATt(users):
    print("Please provide your ip from which your messages will be sent and recieved.")
    ip = input(': ')
    print("What would you like to say?")
    message = input(': ')
    users['ip address'] = ip
    HOST = ip
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall((message))
        data = s.recv(1024)
    print(f"Received {data!r}")


### 345

def connect_to_chat(users):
    print("You are about to connect please login first")
    print("Please print your username")
    name = input(': ')
    if name in users():
        print("Please provide your ip from which your messages will be sent and recieved.")
    ip = input(': ')
    while ip != None:
        if ip in (users['ip'][ip]):
            print("This ip is registered already please enter another one.")
        elif ip not in (users[ip]['ip']):
            print(
                "You have connected to the chat, to leave say '!leave' otherwise you can send messages by pressing Enter")
            print("What would you like to say?")
            message = input(': ')
            while message != '!leave':
                message = (users['message'][message])
                print(users[user][message])

    print("Please enter a valid IPv6")

    ###