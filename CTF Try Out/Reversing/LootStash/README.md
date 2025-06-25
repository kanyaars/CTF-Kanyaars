# Challenge: LootStash (Reversing)

## Challenge Overview

**Name:** LootStash
**Category:** Reversing
**Difficulty:** Very Easy

---

## Challenge Description

> A giant stash of powerful weapons and gear have been dropped into the arena - but there's one item you have in mind. Can you filter through the stack to get to the one thing you really need?

---

# Challenge Progress: LootStash (Reversing)

## Solution Walkthrough

### 1. Basic File Inspection

```bash
file stash
```

Output:

```
stash: ELF 64-bit LSB executable, x86-64
```

The binary is a Linux 64-bit executable.

### 2. Run the Binary

```bash
chmod +x stash
./stash
```

Output:

```
Diving into the stash - let's see what we can find.
.....
You got: 'Dusksong, Whisper of the Covenant'. Now run, before anyone tries to steal it!
```

The output suggests a randomized loot generator selecting from a predefined list of gear.

### 3. Analyze Raw Content

To find anything suspicious (such as a flag embedded inside the binary):

```bash
cat stash
```

Or:

```bash
strings stash | less
```

Inside the file, the following string was revealed:

```
HTB{n33dl3_1n_a_l00t_stack}
```

This is clearly the challenge flag.

---

## 🌊 Final Flag

```
HTB{n33dl3_1n_a_l00t_stack}
```

May god with us~