import os
import socket
from IPy import IP
from pyfiglet import  Figlet
socket.setdefaulttimeout(0.5)
'''def st(n):
    a = n* '<>'
    b = n * '**' + '\n                         CREATED BY LOCKER TEAM' 
    c = n * '**'
    d = n* '><'
    print(f'\n{a}\n{b}\n{c}\n{d}\n')
st(35)'''

text = Figlet(font='slant')
os.system('clear')
os.system('mode con: cols=75 lines=30')
print(text.renderText('LOCKER TEAM'))

usr = input('               | YOU CAN USE LINKS TO SCAN INSTEAD OF AN IP | \n\n\n[+] -t : To Scan Top Ports:  \n\n [+] -a: To Scan All Ports \n\n [+] -p: To Scan A Specified Port\n')
#print(usr)
def ipp(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def scn(ip,port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        print('[+] Port ' + str(port) + ' Is Open')
    except:
        pass
if usr == '-t':
    ip2 = input('\n[+] Enter the target ip: ')
    i2 = ipp(ip2)
    for ports in 20,21,22,23,25,53,80,110,119,123,143,161,194,443:
        scn(ip2, ports)
if usr == '-a':
    ip1 = input('[+]\nEnter The Target Ip: ')
    ip1 = ipp(ip1)
    for port in range(1,2900):
        scn(ip1,port)
elif usr == '-p':
    ip3 = input('\n[+]Enter the target ip to scan: ')
    ip3 = ipp(ip3)
    ask_for_port = int(input('\n[+]Enter The Port Number: '))
    scn(ip3,ask_for_port)

