---
description: Hashes and Passwords
---

# System Attacks

## John the Ripper

### Unshadow

`passwd` is the **/etc/passwd** file  
`shadow` is the **/etc/shadow** file

```text
unshadow passwd shadow > hash
```

### Hash Cracking

```text
john --wordlist=/etc/john/rockyou.txt hash --show
```

Google the commands depending on the hash you find using `hashidentifier`



