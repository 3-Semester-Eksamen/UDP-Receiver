from socket import *
import requests
import json

PORT = 7001
s = socket(AF_INET, SOCK_DGRAM)
s.bind(("", PORT))
print("The UDP receiver is ready to receive")

API_URL = "https://localhost:7220/api/readings"


# Function that gets called once a UDP-Packet is received, and the message parsed.
def handle_msg(msg):
    if msg:
        post_api(json.loads("{" + msg + "}"))


# Function that posts the reading to the Rest API.
def post_api(data):
    print(data)
    if API_URL:
        requests.post(API_URL, json=data)


while True:
    message, client_address = s.recvfrom(2048)
    handle_msg(message.decode())
