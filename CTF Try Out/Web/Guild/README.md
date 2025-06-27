# Challenge: Guild (Web)

## Challenge Overview

**Name:** Guild  
**Category:** Web  
**Difficulty:** Medium

### Description:

Welcome to the Guild ! But please wait until our Guild Master verify you. Thanks for the wait

---

# Challenge Progress: Guild (Web)

## Recon & Initial Steps

### 1. Registering and Logging In

First, create an account by signing up with a random email and password. After logging in, you are prompted to upload a profile picture as part of the verification process.

---

### 2. Profile Section & Vulnerability Discovery

In the **Profile** section, the system allows you to update your biography. Upon analyzing the functionality, it was discovered that the system was vulnerable to **Server-Side Template Injection (SSTI)** via the Jinja template engine. By entering a Jinja template payload in the biography section, we could retrieve sensitive information like the admin's email.

**Payload for retrieving the admin's email:**

```jinja
{{ User.query.filter(User.username=="admin").first().email }}
````

This payload was placed in the biography field, and once the profile was accessed, the admin's email address was successfully retrieved.

---

### 3. Exploiting the Forgotten Password Mechanism

Using the email address of the admin, we exploited the **forgot password** functionality. The system uses a predictable SHA-256 hash of the email to generate a reset link. By hashing the admin's email and visiting the password reset link, we could reset the admin’s password.

**SHA-256 hash of the admin's email:**

```bash
echo -n "53424e6967663068@master.guild" | sha256sum
```

After obtaining the hash, we visited the reset password URL and changed the admin's password.

---

## Verification Process & Final Exploit

### 4. Image Upload and EXIF Metadata Injection

Once logged into the admin account, the verification section was available, requiring a photo upload to validate users. The EXIF metadata of the uploaded image was used for verification. After inspecting the backend, we discovered that the "Artist" field in the EXIF metadata was being used as part of the verification process.

We crafted an **EXIF payload** to exploit the **SSTI** vulnerability and injected a payload into the "Artist" field, which allowed us to execute arbitrary Python code on the server. This ultimately gave us access to execute commands on the server.

**Payload for retrieving the flag:**

```jinja
{% for i in ''.__class__.__mro__[1].__subclasses__() %}
{% if i.__name__ == 'Popen' %}
{{ i(['cat', 'flag.txt'], -1, None, None, -1).communicate()[0] }}
{% endif %}
{% endfor %}
```

This payload dynamically finds the `Popen` class and executes the `cat flag.txt` command, which reveals the contents of the flag.

---

### 5. Uploading the Payload

We injected this payload into the "Artist" field of the EXIF metadata and uploaded the modified image. Upon verifying the image, the flag was displayed.

---

## Flag

```
HTB{mult1pl3_lo0p5_mult1pl3_h0les_290a88c684f7e4b13d806911c57c8d46}
```

---

## Conclusion

This challenge provided an excellent opportunity to practice exploiting **Server-Side Template Injection (SSTI)** and **EXIF metadata manipulation**. The vulnerability allowed us to escalate privileges and execute arbitrary commands on the server, ultimately leading to flag retrieval. The key takeaway is the importance of **sanitizing user input**, especially when it is directly used in templates and file metadata.

May god with us\~

```

May god with us~