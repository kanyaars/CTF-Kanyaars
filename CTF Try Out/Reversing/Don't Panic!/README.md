# Challenge: Don't Panic! (Reversing)

## Challenge Overview

**Name:** Don't Panic!
**Category:** Reversing
**Difficulty:** Easy

### Description:

You've cut a deal with the Brotherhood; if you can locate and retrieve their stolen weapons cache, they'll provide you with the kerosene needed for your makeshift explosives for the underground tunnel excavation. The team has tracked the unique energy signature of the weapons to a small vault, currently being occupied by a gang of raiders who infiltrated the outpost by impersonating commonwealth traders. Using experimental stealth technology, you've slipped by the guards and arrive at the inner sanctum. Now, you must find a way past the highly sensitive heat-signature detection robot. Can you disable the security robot without setting off the alarm?

---

# Challenge Progress: Don't Panic (Reversing)

## Steps to Solve

### 1. Environment Preparation
- Create a virtual environment using: `python3 -m venv venv`
- Activate the environment: `source venv/bin/activate`
- Install `ghidra-bridge`:
  ```bash
  pip install ghidra-bridge --break-system-packages
  ```

### 2. Install ghidra_bridge server
- Run the command:
  ```bash
  python -m ghidra_bridge.install_server ~/ghidra_scripts
  ```

### 3. Run Ghidra
- Download the official release version of Ghidra (not from GitHub source).
- Run `./ghidraRun` and select your installed JDK directory (Java 17+ or ideally JDK 21+).
- Create a new project and import the `dont_panic` binary.
- When prompted, run Auto Analysis with default settings.

### 4. Run ghidra_bridge_server
- Open the Script Manager in Ghidra.
- Execute `ghidra_bridge_server.py` from the `~/ghidra_scripts` directory.

### 5. Connect Python to Ghidra
- Open Python in your virtual environment.
- Run:
  ```python
  import ghidra_bridge
  b = ghidra_bridge.GhidraBridge(namespace=globals())
  ```

### 6. Extract the Flag with Python
- Use the following automation script to extract the flag from the binary:

```python
start_addr = 0x10912d
listing = getState().getCurrentProgram().getListing()
fn_body = getState().getCurrentProgram().getFunctionManager().getFunctionContaining(getAddress(start_addr)).getBody()
instructions = listing.getInstructions(fn_body, True)
result = ['x' for _ in range(35)]
state = {}

print("Extracting RSP Values:")
for instruction in instructions:
    if "LEA" in str(instruction):
        state[str(instruction).split(",")[0].split(" ")[1]] = int(str(instruction).split("[")[1][:-1], 16)
    if "MOV qword ptr" in str(instruction):
        try:
            target = (int(str(instruction).split("RSP + ")[1].split("]")[0], 16) - 16) // 8
            reg = str(instruction).split(",")[1]
            result[target] = chr(int(str(getInstructionAt(getAddress(state[reg] + 1))).split(",")[1],16))
            print(result[target].strip(), end='', flush=True)
        except Exception:
            print()
            exit(0)
```

### 7. Output
After running the script, the flag will appear in the terminal:

```
HTB{d0nt_p4n1c_c4tch_the_3rror}
```

May god with us~