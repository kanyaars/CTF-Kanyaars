# Challenge: TunnelMadness (Reversing)

## Challenge Overview

**Name:** TunnelMadness
**Category:** Reversing
**Difficulty:** Medium

### Description:

Within Vault 8707 are located master keys used to access any vault in the country. Unfortunately, the entrance was caved in long ago. There are decades-old rumors that the few survivors managed to tunnel out deep underground and make their way to safety. Can you uncover their tunnel and break back into the vault?

---

# Challenge Progress: TunnelMadness (Reversing)

## Steps to Solve

### 1. Environment Preparation

* First, ensure you have Python 3 and pip installed in your environment.
* Create a virtual environment:

  ```bash
  python3 -m venv env
  ```
* Activate the virtual environment:

  ```bash
  source env/bin/activate
  ```
* Install necessary libraries:

  ```bash
  pip install pwntools
  ```

### 2. Analyzing the Binary

* The challenge provides a binary file called `tunnel`. We need to analyze it to understand the logic behind the 3D maze and how we can solve it.
* Load the binary in a disassembler like Ghidra or IDA Pro to get a clear view of its structure.
* We discovered that the binary uses a 3D maze and requires us to navigate through it by sending direction commands to the server.
* The available directions are: Left (L), Right (R), Forward (F), Backward (B), Up (U), Down (D), and Quit (Q).

### 3. Understanding the Maze

* The maze is a 20x20x20 grid, and we need to find the path from the start (0, 0, 0) to the end (19, 19, 19).
* Each cell in the maze has a specific state:

  * `0`: Start position
  * `1`: Open cell
  * `2`: Wall
  * `3`: End position
* By analyzing the binary code, we identified how the game mechanics work, where the position is updated based on the direction chosen, and how the maze is stored in memory.

### 4. Writing the Solver Script

* We wrote a Python script to interact with the game, solving the maze programmatically.
* The script leverages the `pwntools` library to interact with the server, send the correct directions, and solve the maze.

### 5. The Solver Algorithm

* We used a depth-first search (DFS) or breadth-first search (BFS) approach to find a path through the maze.
* The script explores the maze by checking all adjacent cells and marking visited cells to avoid re-exploration.
* Once the path is found, we convert the path into a series of directions and send them to the server.

### 6. Final Exploit Script

```python
from pwn import *
import struct

MAZE_SIZE = 20
CELL_SIZE = 0x10

e = ELF("./tunnel", checksec=False)

def read_cell(addr):
    data = e.read(addr, CELL_SIZE)
    return struct.unpack("IIII", data)

def read_coord(coord):
    x, y, z = coord
    addr = e.sym["maze"] + (x * MAZE_SIZE * MAZE_SIZE * CELL_SIZE) + (y * MAZE_SIZE * CELL_SIZE) + (z * CELL_SIZE)
    return read_cell(addr)

START = 0
OPEN = 1
CLOSED = 2
FINISH = 3

def get_adj(pos):
    x, y, z = pos
    options = []
    if not x - 1 < 0: options.append((x-1, y, z))
    if not x + 1 >= MAZE_SIZE: options.append((x+1, y, z))
    if not y - 1 < 0: options.append((x, y-1, z))
    if not y + 1 >= MAZE_SIZE: options.append((x, y+1, z))
    if not z - 1 < 0: options.append((x, y, z-1))
    if not z + 1 >= MAZE_SIZE: options.append((x, y, z+1))
    return options

def solve():
    pos = (0, 0, 0)
    visited = []
    while True:
        for adj in get_adj(pos):
            if adj in visited: continue
            _, _, _, typ = read_coord(adj)
            if typ == OPEN:
                visited.append(pos)
                pos = adj
                break
            elif typ == FINISH:
                return visited + [pos, adj]
        else:
            print(f"failed at {pos}")

path = solve()
solution = ""
for i in range(1, len(path)):
    prev = path[i-1]
    cur = path[i]
    if cur[0] > prev[0]:
        solution += "R"
    elif cur[0] < prev[0]:
        solution += "L"
    elif cur[1] > prev[1]:
        solution += "F"
    elif cur[1] < prev[1]:
        solution += "B"
    elif cur[2] > prev[2]:
        solution += "U"
    elif cur[2] < prev[2]:
        solution += "D"

print(solution)

r = remote('94.237.121.185', 48480)
for c in solution:
    r.sendlineafter(b"? ", c.encode())
print(r.recvlines(2)[1].decode())
```

### 7. Running the Script

* After running the Python script, the path was solved, and the directions were sent to the server. The flag was successfully retrieved.

### 8. Output

After running the script, the terminal displayed the flag:

```
HTB{tunn3l1ng_ab0ut_in_3d_ed1e6e733081fb4de3cdb0119af9af97}
```

May god with us~