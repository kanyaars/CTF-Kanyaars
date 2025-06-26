# Challenge: An Unusual Sighting (Forensics)

## Challenge Overview

**Name:** An Unusual Sighting  
**Category:** Forensics  
**Difficulty:** Very Easy  

## Description

As preparations come to an end and The Fray draws near, our newly formed team has been working on refactoring the CMS application for the competition. However, after some time, we noticed that much of our work had mysteriously disappeared. We managed to extract the SSH logs and bash history from the suspected development server. The faction that uncovers the perpetrator will gain a massive advantage in the competition!

## Provided Artifacts

- `sshd.log` – SSH connection and authentication logs  
- `bash_history.txt` – Bash command history from the suspected server

## Analysis & Findings

1. **SSH Server IP and Port**  
   From the log:  
   `Connection from 100.7.98.129 port 47765 on 100.107.36.130 port 2221`  
   `100.107.36.130:2221`

2. **Timestamp of the First Successful Login**  
   `[2024-02-13 11:29:50] Accepted password for softdev from 100.7.98.129 port 47765`  
   `2024-02-13 11:29:50`

3. **Timestamp of the Unusual Login**  
   `[2024-02-19 04:00:14] Accepted publickey for root from 2.67.182.119 port 60071`  
   `2024-02-19 04:00:14`

4. **Attacker’s Public Key Fingerprint**  
   From failed login logs:  
   `ECDSA SHA256:OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4`  
   `SHA256:OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4`

5. **First Command Executed by the Attacker**  
   From `bash_history.txt`:  
   `[2024-02-19 04:00:18] whoami`  
   `whoami`

6. **Last Command Executed Before Logout**  
   `[2024-02-19 04:14:02] ./setup`  
   `./setup`

## Final Flag

```
HTB{4n_unusual_s1ght1ng_1n_SSH_l0gs!}
```

May god with us~