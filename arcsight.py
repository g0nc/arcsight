#!usr/bin/python
import os
import time
import sys


def banner():

    print("""\n |||| W A R N I N G |||| \n
          the solution will need to restart the system after changes... so.. confirm if you want\n to execute the script now!!!!!""")
    s = raw_input("CONTINUE? Y/N: ")
    if(str(s.upper()) == "Y"):
        verify_system()
    else:
        exit

def verify_system():
    
    os.system("echo '' > system.txt")
    os.system('uname -a > system.txt')
    arquivo = open("system.txt", "r")
    linhas = arquivo.readlines()
    for line in linhas:
        if(str(line.upper()).find("DEBIAN")):
            print("THE SISTEM IS DEBIAN")
            main("1")
        elif(str(line.upper()).find("CENTOS")):
            print("THE SISTEM IS CENTOS")
            main("2")

def main(system):

    try:
        if system == "1":
            time.sleep(2)
            print("Creating group and arcsight user...\n")
            time.sleep(2)
            os.system("groupadd -g 750 arcsight")
            print("Add user to arcsight group")
            time.sleep(2)
            os.system("useradd -m -g arcsight -u 1500 arcsight")
            print("Modify owner path(/opt/arcsight) to arcsight:arcsight")
            os.system("chown -R arcsight:arcsight /opt/arcsight")
            time.sleep(2)
            
            print("Modify limits.conf lines...")
            primeiralinha = "* soft nproc 10240"
            segundalinha = "* hard nproc 10240"
            terceiralinha = "* soft nofile 65536"
            quartalinha = "* hard nofile 65536"
            time.sleep(2)
            
            print("Saving backup....")
            backup = os.system("cp /etc/security/limits.conf /etc/security/limits.conf.bkp")
            time.sleep(1)
            print("Backup Saved...")
            time.sleep(2)
            print("Writing...")
            
            a = os.system('echo '+"'"+primeiralinha+"' >> /etc/security/limits.conf")
            a = os.system('echo '+"'"+segundalinha+"' >> /etc/security/limits.conf")
            a = os.system('echo '+"'"+terceiralinha+"' >> /etc/security/limits.conf")
            a = os.system('echo '+"'"+quartalinha+"' >> /etc/security/limits.conf")
            b = os.system('cat /etc/security/limits.conf')
            
            time.sleep(2)
            print("limits.conf writed [!]")
            time.sleep(3)
            print("rebooting...")
            
           # os.system("reboot")
            
        elif system == "2":
            time.sleep(2)
            print("Creating group and arcsight user...\n")
            os.system("groupadd -g 750 arcsight")
            os.system("useradd -m -g arcsight -u 1500 arcsight")
            os.system("chown -R arcsight:arcsight /opt/arcsight")
            time.sleep(1)
            filename = raw_input("Qual path do arquivo .conf?: ")
            
            backup = os.system("cp "+str(filename)+" "+str(filename)+".bkp")
            primeiralinha = "* soft nproc 10240"
            segundalinha = "* hard nproc 10240"
            terceiralinha = "* soft nofile 65536"
            quartalinha = "* hard nofile 65536"
            
            a = os.system("echo '' > "+str(filename))
            a = os.system('echo '+"'"+primeiralinha+"' >> "+str(filename))
            a = os.system('echo '+"'"+segundalinha+"' >> "+str(filename))
            a = os.system('echo '+"'"+terceiralinha+"' >> "+str(filename))
            a = os.system('echo '+"'"+quartalinha+"' >> "+str(filename))
            
            print("[!]rebooting...")
            #os.system("reboot")
            
        
    except:
        print("An error ocurred, try again !!!")
        
def backup(system):
        if typesystem == "1":
                a  = os.system("cat /etc/security/limits.conf.bkp | > limits.conf")
        elif typesystem == "2":
            a = os.system("cat "+str(filename)+".bkp | >"+str(filename))
        print("you need to reboot your system to changes make effects")

banner()