import telnetlib
import time

host='10.11.11.1'
usename='hack'
password='123456'

tn=telnetlib.Telnet(host,)

tn.read_until(b"username")
tn.write(usename.encode('ascii')+ b"\n")
tn.write(b"password:")
tn.write(password.encode('ascii')+ b"\n")
time.sleep(1)
tn.write(b"system-view \n")
time.sleep(1)
tn.write(b"int g0/0/1 \n")
tn.write(b"ip add 10.0.0.2 8\n")
tn.write(b"dis ip int br")
tn.write(b"vlan batch 10 to 20\n")
time.sleep(1)
tn.close()

