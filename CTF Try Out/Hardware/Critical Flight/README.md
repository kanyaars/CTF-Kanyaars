# Challenge: Critical Flight (Hardware)

## Challenge Overview

**Name:** Critical Flight
**Category:** Hardware
**Difficulty:** Very Easy

### Description:

Your team has been tasked with investigating the production files of Printed Circuit Boards (PCBs) used in DIY drones. These drones are falling out of the sky due to suspected sabotage in the flight controller PCB design. Your mission is to find any irregularities or malicious alterations that could reveal the cause — and ultimately the flag.

---

## Objective

Identify suspicious modifications made to the PCB layout and extract the hidden flag embedded in the board design.

---

## Files Provided

1. **HadesMicro-B_Cu.gbr**
2. **HadesMicro-B_Fab.gbr**
3. **HadesMicro-B_Mask.gbr**
4. **HadesMicro-B_Paste.gbr**
5. **HadesMicro-B_Silkscreen.gbr**
6. **HadesMicro-Edge_Cuts.gbr**
7. **HadesMicro-F_Cu.gbr**
8. **HadesMicro-F_Fab.gbr**
9. **HadesMicro-F_Mask.gbr**
10. **HadesMicro-F_Paste.gbr**
11. **HadesMicro-F_Silkscreen.gbr**
12. **HadesMicro-In1_Cu.gbr**
13. **HadesMicro-In2_Cu.gbr**

---

# Challenge Progress: Critical Flight (Hardware)

## Step-by-Step Walkthrough

### 1. **Extract and Review Files**

* Unzip the challenge file to reveal multiple `.gbr`, 

### 2. **Open with Gerber Viewer**

* Navigate to [PCBWay Online Viewer](https://www.pcbway.com/project/OnlineGerberViewer.html).
* Upload the entire folder or zipped archive.

### 3. **Isolate Key Layers**

* In the viewer, disable all layers initially.
* Enable only the **bottom copper (B.Cu)** layer and **inner copper (In1.Cu)** layers.
* Optionally, inspect **top copper (F.Cu)** or other mechanical layers.

### 4. **Read the Message**

* The flag is split across two layers:
  * The first half is located on the bottom copper layer.
  * The second half is on the inner copper layer.
* By combining both parts, the complete flag is revealed:
  ```
  HTB{533_7h3_1nn32_w02k1n95_0f_313c720n1c5#$@}
  ```

---

## Final Flag

```
HTB{533_7h3_1nn32_w02k1n95_0f_313c720n1c5#$@}
```

May god with us~