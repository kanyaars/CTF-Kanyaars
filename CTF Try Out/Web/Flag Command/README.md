# Challenge: Flag Command (Web)

## Challenge Overview

**Name:** Flag Command
**Category:** Reversing
**Difficulty:** Very Easy

### Description:

Embark on the "Dimensional Escape Quest" where you wake up in a mysterious forest maze that's not quite of this world. Navigate singing squirrels, mischievous nymphs, and grumpy wizards in a whimsical labyrinth that may lead to otherworldly surprises. Will you conquer the enchanted maze or find yourself lost in a different dimension of magical challenges? The journey unfolds in this mystical escape!

---

# Challenge Progress: Flag Command (Web)

## Steps to Solve

### 1. WhatWeb Fingerprinting
```bash
whatweb http://83.136.253.201:42841
```
Result shows the site is powered by `Werkzeug/3.0.1` and `Python 3.11.8`.

### 2. Directory Fuzzing
```bash
ffuf -u http://83.136.253.201:42841/FUZZ -w ./SecLists/Discovery/Web-Content/common.txt -fc 404
```
Found several interesting endpoints:
- `/admin`
- `/debug`
- `/flag`
- `/api`
- `/command`

However, all return:
```json
{ "message": "404 Not Found" }
```

### 3. Source Code Analysis
The page uses a terminal-style interactive game powered by JavaScript. Loaded scripts:
- `/static/terminal/js/commands.js`
- `/static/terminal/js/main.js`
- `/static/terminal/js/game.js`

From `main.js`, the game logic fetches options and sends commands through:
- `/api/options` → returns available commands per stage
- `/api/monitor` → POST endpoint that returns messages or the flag

Fetching all available commands:
```bash
curl -s http://83.136.253.201:42841/api/options
```

Response:
```json
{
  "allPossibleCommands": {
    "1": ["HEAD NORTH", "HEAD WEST", "HEAD EAST", "HEAD SOUTH"],
    "2": ["GO DEEPER INTO THE FOREST", "FOLLOW A MYSTERIOUS PATH", "CLIMB A TREE", "TURN BACK"],
    "3": ["EXPLORE A CAVE", "CROSS A RICKETY BRIDGE", "FOLLOW A GLOWING BUTTERFLY", "SET UP CAMP"],
    "4": ["ENTER A MAGICAL PORTAL", "SWIM ACROSS A MYSTERIOUS LAKE", "FOLLOW A SINGING SQUIRREL", "BUILD A RAFT AND SAIL DOWNSTREAM"],
    "secret": ["Blip-blop, in a pickle with a hiccup! Shmiggity-shmack"]
  }
}
```

### 4. Exploitation

The user interface accepts input like a terminal. The correct sequence of commands that leads to success is:

1. `start`
2. `HEAD NORTH`
3. `FOLLOW A MYSTERIOUS PATH`
4. `SET UP CAMP`
5. `FOLLOW A SINGING SQUIRREL`

Upon success, the backend responds with a message containing the flag.

---

## Flag

```
HTB{D3v3l0p3r_t00l5_4r3_b35t_wh4t_y0u_Th1nk??!_37ca95a0744f02bb5ed61af633c314f9}
```

GGWP!!!!1