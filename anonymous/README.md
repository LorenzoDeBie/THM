# Anonymous

```bash
export IP=10.10.51.40
```

[nmap output](nmap/initial)
* 21: ftp
* 22: ssh
* 139 & 445: netbios-ssn Samba smbd 3.X - 4.X

## Task 1: Pwn
**Enumerate the machine.  How many ports are open?**
```
4
```

**What service is running on port 21?**
```
ftp
```

**What service is running on ports 139 and 445?**
```
smb
```

**There's a share on the user's computer.  What's it called?**
```
pics
```
[nmap smb scan results](nmap/smb445)

**user.txt**
```
90d6f992585815ff991e68748c414740
```
added bash revshell to clean.sh on ftp server, this script gets executed every couple of minutes --> user access

**root.txt**
```
4d930091c31a622a7ed10f27999af363
```
env has suid bit set --> ez root shell with:
```
env /bin/bash -p
```

