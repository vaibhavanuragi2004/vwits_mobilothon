import socket

# DSRC V2V Example
HOST = '192.168.0.1'  # IP of the vehicle's DSRC module
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received data from {addr}: {data.decode()}")
