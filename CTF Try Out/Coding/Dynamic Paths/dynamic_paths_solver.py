import socket
import re

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

# Koneksi ke server
HOST = "94.237.122.164"
PORT = 45007

with socket.create_connection((HOST, PORT)) as s:
    f = s.makefile("rw", buffering=1, encoding="utf-8")

    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())

        # Cek apakah kita di tahap soal
        if re.match(r"Test \d+/\d+", line):
            size_line = f.readline().strip()
            print(size_line)
            match = re.match(r"(\d+)\s+(\d+)", size_line)
            if not match:
                continue

            rows, cols = map(int, match.groups())

            number_line = f.readline().strip()
            print(number_line)
            numbers = list(map(int, number_line.split()))
            if len(numbers) != rows * cols:
                print("[!] Jumlah elemen tidak sesuai ukuran grid")
                continue

            # Bentuk grid dan solve
            grid = [numbers[i * cols:(i + 1) * cols] for i in range(rows)]
            result = solve_min_path_sum(grid, rows, cols)
            print(f"> {result}")
            f.write(f"{result}\n")
