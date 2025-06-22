import ctypes
from pwn import *

libc = ctypes.CDLL("libc.so.6")
casino = ELF("./casino", checksec=False)

mapping = {}
for i in range(255):
    libc.srand(i)
    mapping[libc.rand()] = chr(i)

flag = ""
check_addr = int(casino.symbols["check"])

for b in range(29):
    addr = check_addr + (b * 4)
    chunk = casino.read(addr, 4)
    val = u32(chunk)  # ✅ INI yang benar (bukan casino.u32)
    flag += mapping[val]

print("Flag:", flag)
