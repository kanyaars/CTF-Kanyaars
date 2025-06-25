# Challenge: Dynastic (Crypto)

## Challenge Overview

**Name:** Dynastic
**Category:** Crypto
**Difficulty:** Very Easy

### Description:

You find yourself trapped inside a sealed gas chamber, and suddenly, the air is pierced by the sound of a distorted voice played through a pre-recorded tape. Through this eerie transmission, you discover that within the next 15 minutes, this very chamber will be inundated with lethal hydrogen cyanide. As the tape’s message concludes, a sudden mechanical whirring fills the chamber, followed by the ominous ticking of a clock. You realise that each beat is one step closer to death. Darkness envelops you, your right hand restrained by handcuffs, and the exit door is locked. Your situation deteriorates as you realise that both the door and the handcuffs demand the same passcode to unlock. Panic is a luxury you cannot afford; swift action is imperative. As you explore your surroundings, your trembling fingers encounter a torch. Instantly, upon flipping the switch, the chamber is bathed in a dim glow, unveiling cryptic letters etched into the walls and a disturbing image of a Roman emperor drawn in blood. Decrypting the letters will provide you the key required to unlock the locks. Use the torch wisely as its battery is almost drained out!

# Dynastic

## Challenge Description

> You find yourself trapped inside a sealed gas chamber, and suddenly, the air is pierced by the sound of a distorted voice played through a pre-recorded tape. Through this eerie transmission, you discover that within the next 15 minutes, this very chamber will be inundated with lethal hydrogen cyanide.  
>  
> As the tape’s message concludes, a sudden mechanical whirring fills the chamber, followed by the ominous ticking of a clock. You realise that each beat is one step closer to death. Darkness envelops you, your right hand restrained by handcuffs, and the exit door is locked.  
>  
> Your situation deteriorates as you realise that both the door and the handcuffs demand the same passcode to unlock. Panic is a luxury you cannot afford; swift action is imperative.  
>  
> As you explore your surroundings, your trembling fingers encounter a torch. Instantly, upon flipping the switch, the chamber is bathed in a dim glow, unveiling cryptic letters etched into the walls and a disturbing image of a Roman emperor drawn in blood.  
>  
> Decrypting the letters will provide you the key required to unlock the locks. Use the torch wisely as its battery is almost drained out!

**Category**: Crypto  
**Points**: 925  
**Difficulty**: Very Easy  
**Files Provided**:
- `output.txt`
- `source.py`

---

## Analysis

The file `output.txt` contains the following encrypted string:

```
DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL
```

And `source.py` includes an encryption function:

```python
def encrypt(m):
    c = ''
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha():
            ech = ch
        else:
            chi = to_identity_map(ch)
            ech = from_identity_map(chi + i)
        c += ech
    return c
```

This is essentially a **Trithemius cipher**, which is a variant of the Caesar cipher where the shift increases based on the character's position (i.e., +0, +1, +2, ...).

---

## Solution

We write a simple decryption script that reverses the encryption logic:

```python
def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def decrypt(m):
    p = ''
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha():
            dch = ch
        else:
            chi = to_identity_map(ch)
            dch = from_identity_map(chi - i)
        p += dch
    return p

encrypted = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"
decrypted = decrypt(encrypted)
print(f"HTB{{{decrypted}}}")
```

### Output:

```
HTB{DID_YOU_KNOW_ABOUT_THE_TRITHEMIUS_CIPHER?!_IT_IS_SIMILAR_TO_CAESAR_CIPHER}
```

---

## Flag

```
HTB{DID_YOU_KNOW_ABOUT_THE_TRITHEMIUS_CIPHER?!_IT_IS_SIMILAR_TO_CAESAR_CIPHER}
```
May god with us~