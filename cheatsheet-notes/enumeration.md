---
description: Information Gathering and Footprinting & Scanning
---

# Enumeration

## whois

```bash
whois foo.bar
```

## subdomains

```bash
sublit3r -d foo.bar
```

## ping sweeps

```bash
fping -a -g 10.10.10.0/24
```

```bash
nmap -sS -n 10.10.10.0/24
```

## Nmap

### OS Fingerprinting

```bash
nmap -Pn -A -O 10.10.10.10
```

### Quick scan 

```bash
nmap -sC -sV -A -T4 10.10.10.10 --open
```

### Full scan

```bash
nmap -sC -sV -A -T4 -p- 10.10.10.10 --open
```

