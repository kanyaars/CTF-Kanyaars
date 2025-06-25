# Challenge: Shush Protocol

## Overview

**Name:** Shush Protocol
**Category:** ICS  
**Difficulty:** Very Easy  

### Description:

Spawn the provided Docker environment, connect to the given IP, and retrieve the flag to confirm your setup is working.
A seemingly inactive PLC (Programmable Logic Controller) buried inside an abandoned fertilizer plant still transmits data over the network. After capturing traffic between the control device and the PLC, your task is to locate the packet that contains the password used by the control device — ultimately revealing the flag.

---

## Objective

Analyze the provided network capture file to extract the password used in a custom protocol for PLC diagnostics and retrieve the flag.

---

# Challenge Progress: Shush Protocol (ICS)

## Steps to Solve

### 1. Open the Capture
- Load `traffic.pcapng` in Wireshark.

### 2. Protocol Analysis
- Observed that most packets use **Modbus/TCP**.
- Noticed the presence of many packets using **Function Code = 102**, which is **not a standard Modbus code** — indicating a possible **custom extension or protocol misuse**.

### 3. Identify Suspicious Packet
- Sorted the packets by **Length** to find the longest payloads.
- Located a unique packet with **Length = 123**, significantly larger than others.
- The Modbus data contained a long hex string:

```
00102e4854427b35306d3337316d33355f63753537306d5f70323037306330315f3432335f6e30375f336e30753968377d
```

### 4. Decode the Payload
- Stripped the leading `00102e` (likely part of the custom header).
- Converted the remaining hex:

```
4854427b35306d3337316d33355f63753537306d5f70323037306330315f3432335f6e30375f336e30753968377d
```

- Resulting ASCII output:

```
HTB{50m371m35_cu570m_p2070c01_423_n07_3n0u9h7}
```

## Final Flag

```
HTB{50m371m35_cu570m_p2070c01_423_n07_3n0u9h7}
```

May god with us~