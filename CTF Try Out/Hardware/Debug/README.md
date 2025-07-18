# Challenge: Debug (Hardware)

## Challenge Overview

**Name:** Debug
**Category:** Hardware
**Difficulty:** Easy

### Description:

Your team has recovered a satellite dish used to transmit the relic’s location. However, it’s malfunctioning due to unknown interference. The debugging interface outputs serial data during the boot process, but no one has been able to decode it — that’s your mission.

---

## Objective

Decode the captured serial signal from the .sal file to identify the interference source and retrieve the flag.

---

## Files Provided

1. **hw_debug.sal** 

---

# Challenge Progress: Debug (Hardware)

## Steps to Solve

### 1. Inspect the Provided File

* The file `hw_debug.sal` is a logic capture file from a Saleae logic analyzer.
* It likely contains UART (serial) communication logs.

### 2. Open File in Logic Analyzer

* Launch **Saleae Logic 2**.
* Open the `hw_debug.sal` file.

### 3. Add Async Serial Analyzer

* Go to the analyzers panel.
* Add an **Async Serial** analyzer to the active channel (usually Channel 0).

### 4. Configure Serial Parameters

* Baud Rate: `115200`
* Data Bits: `8`
* Parity: `None`
* Stop Bits: `1`

### 5. Decode and Review Output

* Enable the **Terminal View** to visualize the decoded ASCII output.
* Scroll through the boot log text to locate any suspicious messages.
* Near the end of the log, a debug message includes the flag.

### 6. Extract the Flag

```
HTB{547311173_n37w02k_c0mp20m153d}
```

---

## Conclusion

This challenge involved forensic signal analysis of embedded system logs.
By applying proper serial decoding, we were able to read the debug boot output and identify a compromised satellite network, along with retrieving the embedded flag.

---

## Flag

```
HTB{547311173_n37w02k_c0mp20m153d}
```

May god with us~