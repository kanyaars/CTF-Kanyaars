# Challenge: Dynamic Paths (Coding)

## Challenge Overview

**Name:** Dynamic Paths
**Category:** Coding
**Difficulty:** Easy

### Description:

On your way to the vault, you decide to follow the underground tunnels, a vast and complicated network of paths used by early humans before the great war. From your previous hack, you already have a map of the tunnels, along with information like distances between sections of the tunnels. While you were studying it to figure your path, a wild super mutant behemoth came behind you and started attacking. Without a second thought, you run into the tunnel, but the behemoth came running inside as well. Can you use your extensive knowledge of the underground tunnels to reach your destination fast and outrun the behemoth?

---

# Challenge Progress: Dynamic Paths (Coding)

## Summary

This challenge gives you 100 test cases. Each test case is a grid of size `i x j` (2 ≤ i, j ≤ 100). Each cell contains a number (1 ≤ n ≤ 50) representing the traversal cost. You start at the top-left corner and can only move **right** or **down**. Your task is to find the minimum path sum to reach the bottom-right corner.

---

## Example

### Input:
```
4 3
2 5 1 9 2 3 9 1 3 11 7 4
```

### Grid:
```
2   5   1
9   2   3
9   1   3
11  7   4
```

### Optimal Path:
2 → 5 → 2 → 1 → 3 → 4 = **17**

---

## Solution

To solve this, we use **Dynamic Programming**. We create a `dp` table where `dp[i][j]` represents the minimum cost to reach cell `(i, j)`.

### Python Script:
```python
import socket

def solve_min_path_sum(grid, rows, cols):
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[-1][-1]

s = socket.socket()
s.connect(("94.237.122.164", 45007))

while True:
    data = b""
    while not data.endswith(b"> "):
        data += s.recv(4096)
    print(data.decode(), end="")

    lines = data.decode().splitlines()
    if "HTB{" in data.decode():
        break

    try:
        dim_line = next(line for line in lines if line.strip() and ' ' in line and all(x.isdigit() for x in line.strip().split()))
        i, j = map(int, dim_line.strip().split())
        nums_line = next(line for line in lines if all(x.isdigit() for x in line.strip().split()))
        nums = list(map(int, nums_line.strip().split()))
        grid = [nums[k * j:(k + 1) * j] for k in range(i)]
        result = solve_min_path_sum(grid, i, j)
        s.sendall(f"{result}\n".encode())
    except Exception as e:
        print(f"\n[ERROR] {e}")
        break

s.close()
```

---

## Flag

```
HTB{b3h3M07H_5h0uld_H4v3_57ud13D_dYM4m1C_pr09r4mm1n9_70_C47ch_y0u_7f66828bac444a15fa0b82c3216e0fb5}
```

NICE CATCHHHH BROOOO!!~~