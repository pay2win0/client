import socket

target_host = " " /ip

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#UDP connectionless/no call
client.sendto(b" ",/enter here (target_host,target_port))

data, addr = client.recvfrom(4096)

print(data.decode()))

client.close()
