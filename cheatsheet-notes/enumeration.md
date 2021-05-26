---
description: Information Gathering and Footprinting & Scanning
---

# Enumeration

## whois

```text
whois foo.bar
```

## subdomains

```text
sublit3r -d foo.bar
```

## ping sweeps

```text
fping -a -g 10.10.10.10
```

```text
nmap -sn 10.10.10.10
```

## Nmap

### OS Fingerprinting

```text
nmap -Pn -A -O 10.10.10.10
```

### Quick scan

```text
nmap -sC -sV -A -T4 10.10.10.10
```

### Full scan

```text
nmap -sC -sV -A -T4 -p- 10.10.10.10
```

