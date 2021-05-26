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
nmap -Pn -O 10.10.10.10
```



