# Challenge: Character (Misc)

## Challenge Overview

**Name:** Character  
**Category:** Misc  
**Difficulty:** Very Easy

### Description:

Security through Induced Boredom is a personal favourite approach of mine. Not as exciting as something like The Fray, but I love making it as tedious as possible to see my secrets, so you can only get one character at a time!

---

# Challenge Progress: Character (Misc)

## Recon & Enumeration

### Initial Scanning

```bash
# We connect to the provided service and start interacting with it.
nc <IP> <PORT>
````

**Result:**
We establish a connection with the service and are able to communicate with it using the `nc` command.

---

## Service Interaction

After connecting, the service prompts for an index and returns the corresponding character from the flag:

```bash
Which character (index) of the flag do you want? Enter an index:
```

We can send the index number and collect the character at that position in the flag. This process is repeated for every character of the flag.

---

## Exploitation - Flag Retrieval

### Process

1. Start from index 0 and continue querying until we get the full flag.
2. We use a Python script to automate this process, querying each index and appending the character returned by the server.

```python
from pwn import *

p = remote('<IP>', <PORT>)
flag = ''
idx = 0
while True:
    p.sendlineafter(b'index: ', str(idx).encode())
    p.recvuntil(b': ')
    char = p.recv(1)

    flag += char.decode()
    idx += 1

    if char == b'}':
        break

print(flag)
```

This script connects to the remote service, queries each index, and appends the resulting character to the `flag` variable. The process continues until we receive the closing curly brace `}`.

---

## Flag

```
HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!}
```

May god with us~