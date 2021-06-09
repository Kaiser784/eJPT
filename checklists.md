---
description: Won't be uploaded
---

# Checklists

If you find a web page of any kind run dirbuster on it doesn't matter if that webpage is the result of a previous scan.

Use Owasp ZAP for spidering and burpsuite for everything else.

Scan technique

ping sweep nmap scan -&gt; full scan for all ip's & quick scan for each ip separately   
Full scan of all ip's will give output after scanning all of them, so you'll have something to work on until then from the quick scans, the ping sweep is to give you a rough idea what the machines are about and also which ip's are alive.

If you're unable to understand what to do with the service you found during your scans use the below site.

{% embed url="https://book.hacktricks.xyz/" %}

For every login prompt try default creds or some other basic ones you find on the net.

If you find ssh or ftp try to login to them with some creds\(needn't be correct\) the banners might give you some idea of what's going on. Use the team names you find on the sites and blog editors.

Metasploit usage is not restricted, use it to the fullest potential.

phpinfo\(\);
