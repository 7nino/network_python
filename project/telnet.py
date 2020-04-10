# -*- coding=utf-8 -*-
from telnetlib import Telnet
import time
def TelentClient(ip,username,password,enable,*cmds):
    tn=Telnet(ip,23)
    rackerply=tn.expect([],timeout=1)[2].decode().strip()
    print(rackerply)
    tn.write(username.encode())
    tn.write(b'\n')
    time.sleep(1)
    rackerply=tn.expect([],timeout=1)[2].decode().strip()
    print(rackerply)
    tn.write(password.encode())
    tn.write(b'\n')
    time.sleep(1)
    rackerply=tn.expect([], timeout=1)[2].decode().strip()
    print(rackerply)
    tn.write(b'enable\n')
    time.sleep(1)
    rackerply=tn.expect([],timeout=1)[2].decode().strip()
    print(rackerply)
    tn.write(enable.encode())
    tn.write(b'\n')
    time.sleep(1)
    rackerply = tn.expect([], timeout=1)[2].decode().strip()
    print(rackerply)
    for cmd in cmds:
        tn.write(cmd.encode())
        tn.write(b'\n')
        rackerply=tn.expect([],timeout=1)[2].decode().strip()
        print(rackerply)
        time.sleep(1)
    tn.write(b'exit\n')
    rackerply=tn.expect([],timeout=1)[2].decode().strip()
    print(rackerply)
    tn.close()
if __name__ == "__main__":
    TelentClient('192.168.100.10','cisco','cisco','cisco','terminal length 0','config t','int f0/1','no sw','ip add 192.168.10.10 255.255.255.0')



