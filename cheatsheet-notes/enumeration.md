---
description: Information Gathering and Footprinting & Scanning
---

# Enumeration

### whois

```text
whois foo.bar
```

### subdomains

```text
sublit3r -d foo.bar
```

### ping sweeps

```text
fping -a -g 10.10.10.10
```

```text
nmpa -sn 10.10.10.10
```

#### Multiple host ping sweep using Nmap

{% tabs %}
{% tab title="hosts.txt" %}
10.10.10.10  
10.10.10.20  
10.10.10.30
{% endtab %}
{% endtabs %}

```text
nmap -sn -iL hosts.txt
```

