# Challenge: Locked Away (Misc)

## Challenge Overview

**Name:** Locked Away  
**Category:** Misc  
**Difficulty:** Easy

### Description:

A test! Getting onto the team is one thing, but you must prove your skills to be chosen to represent the best of the best. They have given you the classic - a restricted environment, devoid of functionality, and it is up to you to see what you can do. Can you break open the chest? Do you have what it takes to bring humanity from the brink?

---

# Challenge Progress: Locked Away (Misc)

## Recon & Enumeration

### Initial Scanning

```bash
nc 94.237.120.190 51554
```

**Result:**
We are presented with a Python-based shell interface that evaluates input using `exec()` after checking against a blacklist.

---

## Service Analysis

### Source Code Review

The challenge provides a Python script (`main.py`) with the following characteristics:

* It displays an ASCII banner.
* A blacklist is defined that prevents input containing keywords such as `open`, `print`, `eval`, `exec`, `flag`, `txt`, and symbols like `[`, `]`, `"`, `'`, etc.
* User input is checked against the blacklist and executed via `exec()` if allowed.
* A function `open_chest()` exists, which opens `flag.txt` and prints its content.
* The goal is to invoke `open_chest()` without triggering the blacklist.

---

## Exploitation - Bypassing the PyJail

### Step-by-step Exploitation

1. **Clear the blacklist**
   The blacklist is implemented as a Python list. Instead of trying to redefine it (which uses `[` and `]`), we call its `.clear()` method to remove all elements without using any blacklisted characters.

2. **Call the `open_chest()` function**
   After clearing the blacklist, we can safely call `open_chest()` to read and print the flag.


```python
blacklist.clear();open_chest()
```

We input this payload into the challenge prompt and the flag is printed as output.

---

## Flag

```
HTB{bYp4sSeD_tH3_fIlT3r5?_aLw4Ys_b3_c4RefUL!_ef6b0d66fac78bc263fa60c2f6b2f1fe}
```

May god with us~