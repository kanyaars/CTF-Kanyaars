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

---

Simple, effective use of PCB visualization to catch hardware-based sabotage!