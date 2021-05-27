# Web Attacks

## Banner grabbing

### Netcat \(for HTTP services\)

```text
nc -v 10.10.10.10 port
HEAD / HTTP/1.0
```

### OpenSSL \(for HTTPS services\)

```text
openssl s_client -connect 10.10.10.10:443
HEAD / HTTP/1.0
```

### Httprint

```text
httprint -P0 -h 10.10.10.10 -s /usr/share/httprint/signatures.txt
```

