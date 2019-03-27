import socket
import os
import sys
import csv

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

framework = raw_input(">DE'DSEC:/ ")
os.chdir("/root/Framework/exploit")
os.system(framework)
def framework_use():
	framework = raw_input(">DE'DSEC:/ ")
	os.system(framework)
def use(exploit):
	exploit = os.chdir("/root/Framework/exploit")
	os.system("cat modules")
if framework == "show modules":
	#os.system("cat modules")
	#path = ("lib")
	#csv.reader(path)
	#os.system("ls")
	diretorio = os.chdir("/root/Framework/exploit")
	os.system("cat modules")
	#print diretorio
	print("agora selecione o module para o exploit") 
	framework = raw_input(">DE'DSEC:/ ")
	os.system(framework)
if "use exploit/python/backdoor_listener" in framework:
	os.chdir("/root/Desktop/Framework/exploit/python")
	framework = raw_input(">DE'DSEC:/(exploit/python/backdoor_listener): ")
	os.system("./backdoor_listener.sh")
if "create exploit/python/backdoor" in framework:
	os.chdir("/root/Framework/exploit/python")
	os.system("python backdoor.py")
if "windowsc" in framework:
	print("[+]Esse Compilador e somente para o python(py to EXE)")
	path = raw_input(">DE'DSEC:/(WindowsCompiler): Insira o caminho do seu malware(Junto com o nome dele) ")
	os.chdir("/root/Framework/exploit/pyinstaller")
	#nome = raw_input(">DE'DSEC:/(WindowsCompiler): Insira o nome do seu malware ")
	os.system("./pyinstaller.py --buildpath=/root/Framework/Malware -p /root/Desktop/Framework/Malware -y -F --noconsole " + path)
if "use exploit/ssh/UploadArchive" in framework:
	os.chdir("/root/Framework/exploit/ssh")
	os.system("python UploadArchive.py")
if "use exploit/scan/scan-port" in framework:
        os.chdir("/root/Framework/exploit/scan")
        os.system("python scan-port.py")
