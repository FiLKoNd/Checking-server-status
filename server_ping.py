# Created by FiLKoNd
import socket, winsound
from colorama import Fore
i = 0
host = input("Enter server ip: ")
my_list = host.split(':')
ip = host[0]
count = (len(my_list))
if count < 2:
    port = 25565
else:
    port = my_list[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while i < 1:
    try:
        print(Fore.RED + 'Server is down')
        s.connect((host, port))
        print(Fore.GREEN + 'The server is up and running.')
        winsound.Beep(1000, 700)
        i += 1
    except:
        continue
input('')