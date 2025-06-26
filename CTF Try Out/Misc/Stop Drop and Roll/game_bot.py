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
    ip, port = '83.136.249.246', 54470
    game = connect_to_game(ip, port)
    e
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