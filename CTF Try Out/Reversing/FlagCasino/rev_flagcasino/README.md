# Challenge Progress: FlagCasino (Reversing)

## Solution Steps

### 1. Binary Analysis

Initial commands:

```bash
file casino
checksec --file=casino
nm casino | grep check
```

Findings:

* The binary is a 64-bit ELF executable with symbols not stripped.
* Global symbol found:

  ```
  0000000000004080 D check
  ```
* This symbol is likely an array of integers generated using `rand()`.

---

### 2. Running the Binary

```bash
chmod +x casino
./casino
```

Output shows a casino animation and a prompt for numeric input:

```
[*** PLEASE PLACE YOUR BETS ***]
> 52
[ * INCORRECT * ]
```

No further clues are provided, confirming that the correct input must be computed, not guessed.

---

### 3. Setting Up Python Environment

To avoid system-managed Python limitations, a virtual environment was created:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pwntools
```

---

### 4. Reverse Engineering the PRNG (rand)

Using Python and `pwntools`, a script was written to simulate the same `rand()` behavior and map each generated value to its original character:

```python
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
    val = u32(chunk)
    flag += mapping[val]

print("Flag:", flag)
```

---

### 5. Executing the Script

```bash
python reverse.py
```

Output:

```
Flag: HTB{...actual_flag_here...}
```

---

## 🧰 Tools Used

* WSL (Ubuntu 24.04)
* `file`, `nm`, `checksec`, `xxd`
* Python 3.12 with `pwntools`
* libc PRNG (`srand`, `rand`) mapping

Good Job~