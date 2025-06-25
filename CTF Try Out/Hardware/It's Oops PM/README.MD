# Challenge: It's Oops PM (Hardware)

## Challenge Overview

**Name:** It's Oops PM
**Category:** Hardware
**Difficulty:** Very Easy

### Description:

The crew finds a cache of environmental sensors that communicate with a satellite. Upon analyzing the embedded logic (simulated using VHDL), they discover a crypto-processor with a suspected backdoor. The challenge is to connect to the satellite and activate it.

---

## Objective

Identify the correct 16-bit binary input that triggers the backdoor in the simulated chip and retrieve the flag.

---

## Files Provided

1. **backdoor.vhdl**
2. **encryption.vhdl**
3. **key.vhdl**
4. **tpm.vhdl**
5. **schematic.png**

---

# Challenge Progress: It's Oops PM (Hardware)

## Static Analysis

### backdoor.vhdl

```vhdl
constant pattern : STD_LOGIC_VECTOR(15 downto 0) := "1111111111101001";
```

* The backdoor is triggered when `D = 0xFFE9`

### encryption.vhdl

* XOR logic is applied, except for bits 0, 6, and 13 which are negated (`NOT K(i)`) before output.

### key.vhdl

```vhdl
constant key : STD_LOGIC_VECTOR(15 downto 0) := "0110001111100001"; -- 0x63E1
```

### tpm.vhdl

* If the backdoor is triggered (`B = '1'`), the chip outputs the key directly.
* Otherwise, the output is the result of encryption logic.

---

## Exploiting the Backdoor

While connecting to the provided server:

```bash
$ nc 94.237.48.12 40338
The input must be a binary signal of 16 bits.
```

### Trial Inputs:

```bash
Input : 0000000000000000
Output: 0100001110100000

Input : 1111111111101001
Output: 0110001111100001
You triggered the backdoor here is the flag: HTB{4_7yp1c41_53cu23_TPM_ch1p}
```

---

## Final Flag

```
HTB{4_7yp1c41_53cu23_TPM_ch1p}
```

---

## Conclusion

* The 16-bit binary input `1111111111101001` (equivalent to `0xFFE9`) activates the backdoor.
* When triggered, the chip directly outputs the key `0x63E1` instead of the encrypted result.
* The challenge is solved by understanding and identifying the backdoor activation condition within the VHDL code and sending that input to the server.

May god with us~