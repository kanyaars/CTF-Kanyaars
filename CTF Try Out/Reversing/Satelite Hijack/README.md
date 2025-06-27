# Challenge: Satellite Hijack (Reversing)

## Challenge Overview

**Name:** Satellite Hijack  
**Category:** Reversing  
**Difficulty:** Hard  

### Description:

The crew has located a dilapidated pre-war bunker. Deep within, a dusty control panel reveals that it was once used for communication with a low-orbit observation satellite. During the war, actors on all sides infiltrated and hacked each others systems and software, inserting backdoors to cripple or take control of critical machinery. It seems like this panel has been tampered with to prevent the control codes necessary to operate the satellite from being transmitted - can you recover the codes and take control of the satellite to locate enemy factions?

---

# Challenge Progress: Satellite Hijack (Reversing)

## Steps to Solve

### 1. Analyze the binary dependencies
- Run `ldd satellite` to confirm that the binary dynamically loads `./library.so`.

### 2. Analyze main binary logic
- Identify the use of the function `send_satellite_message()` from the library.
- Understand that it’s an `ifunc` resolver by inspecting the output of `nm -D library.so`.

### 3. Analyze the ifunc mechanism in `library.so`
- Recognize that `send_satellite_message` is resolved dynamically depending on the presence of a custom environment variable:

```c
  SAT_PROD_ENVIRONRONMENT
```

### 4. Set the environment variable

```bash
export SAT_PROD_ENVIRONRONMENT=1
```

### 5. Reverse engineer GOT overwrite

* The `ifunc` resolver returns the address of a memory page with executable permission.
* A chunk of XOR-encrypted shellcode is loaded using `memfrob()` and replaces the GOT entry of `read`.

### 6. Extract and decode the injected code

* Dump the `data_11a9` section containing 0x1000 bytes of encrypted code.
* Decode it with:

```python
from pwn import *

buf = bytearray(b"l5{0v0Y7fVf?u>|:O!|Lx!o$j,;f")
for i in range(len(buf)):
    buf[i] ^= i

print((b"HTB{" + buf).decode())
```

### 7. Get the flag

* Running the script yields the flag:

```
HTB{l4y3r5_0n_l4y3r5_0n_l4y3r5!}
```

May god with us~