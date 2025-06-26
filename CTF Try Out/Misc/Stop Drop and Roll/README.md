# Challenge: Stop Drop and Roll (Misc)

## Challenge Overview

**Name:** Stop Drop and Roll
**Category:** Misc
**Difficulty:** Very Easy

### Description:

In the **Stop Drop and Roll** challenge, you must respond to a series of scenarios with the correct actions. The game will give you a series of words like **GORGE**, **PHREAK**, and **FIRE**, and you need to send back the corresponding actions:

* **GORGE** → **STOP**
* **PHREAK** → **DROP**
* **FIRE** → **ROLL**

If multiple scenarios are provided, you need to respond with a sequence of actions, such as: `STOP-ROLL-DROP`. If you provide the correct sequence of actions for all the scenarios, you will receive the flag.

---

# Challenge Progress: Stop Drop and Roll (Misc)

## Recon & Enumeration

### Initial Scanning

```bash
nc 94.237.56.47 47142
```

**Result:**
We successfully establish a connection to the remote service on the given IP and port. The service prompts us to start the game and asks if we are ready to begin.

---

## Service Interaction

After connecting, the game presents a series of scenarios. For each one, we need to respond with the corresponding action. The game can provide one or more scenarios, and we must send back the actions in the correct order.

**Example Input:**

```
GORGE, FIRE, GORGE, PHREAK, FIRE
```

**Expected Response:**

```
STOP-ROLL-STOP-DROP-ROLL
```

---

## Exploitation - Automating the Process

### Problem

Manually typing the responses for each scenario could be tedious. To automate this, we wrote a Python script that connects to the service, reads the scenarios, processes the scenarios, and sends the correct responses back.

### Solution

We created a Python script using the **Pwntools** library to interact with the game. The script:

1. Connects to the service.
2. Waits for the game prompt and responds with `y` to start.
3. Receives the scenario(s), processes them, and sends the correct sequence of actions.
4. Repeats the process until the game ends.

### Python Script

```python
from pwn import *

ACTION_MAPPING = {
    "GORGE": "STOP",
    "PHREAK": "DROP",
    "FIRE": "ROLL"
}

def connect_to_game(ip, port):
    return remote(ip, port)

def process_scenario(scenario_line):
    scenarios = scenario_line.strip().decode().split(", ")
    return "-".join([ACTION_MAPPING.get(scenario, "") for scenario in scenarios])

def run_game():
    ip, port = '94.237.56.47', 47142
    game = connect_to_game(ip, port)
    
    game.sendlineafter(b'(y/n) ', b'y')
    game.recvline()  

    while True:
        scenario_line = game.recvline()
        decoded_line = scenario_line.strip().decode()

        if 'GORGE' not in decoded_line and 'PHREAK' not in decoded_line and 'FIRE' not in decoded_line:
            print(f"Game over: {decoded_line}")
            break

        response = process_scenario(scenario_line)

        game.sendlineafter(b'do? ', response.encode())

if __name__ == "__main__":
    run_game()
```

---

## Flag

After running the script and successfully completing the game, the flag was retrieved:

```
HTB{1_wiLl_sT0p_dR0p_4nD_r0Ll_mY_w4Y_oUt!}
```

May god with us~