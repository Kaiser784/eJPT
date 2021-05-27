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

## HTTP Verbs

`GET,  POST, HEAD, PUT, DELETE`

### PUT is used to upload a file to the server

You have to find the size of the file you are uploading first

```text
wc -m payload.php
[size] payload.php
```

```text
nc 10.10.10.10 80
PUT /payload.php
Content-type: text/html
Content-length: [size]

```

### DELETE is used to delete a file from the server

```text
nc 10.10.10.10 80
DELETE /path/to/file.txt / HTTP/1.0
```

### OPTIONS is used to query the webserver for enabled HTTP Verbs

```text
nc 10.10.10.10 80
OPTIONS / HTTP/1.0
```

## Directory and File scanning

I'm more used to Dirbuster than dirb or gobuster and also you can change the view in results to be tree file structure which is more convenient.

![Dirbuster](../.gitbook/assets/dirbuster.png)

1. You can choose different wordlists for the dictionary brute force but from my experience in most labs you can find them in the `common.txt` 
2. You can also choose different extensions but php and bak will be the most useful ones to find.

