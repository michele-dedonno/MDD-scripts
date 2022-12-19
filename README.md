# Scripts

Collection of scripts for different purposes, mainly for Capture The Flags, Penetration Testing, and Security Assessments.

* [AD-enum.ps1](AD-enum.ps1): PowerShell script that implements basic Active Directory enumeration when executed on a domain-joined machine;
* [fuzz.py](fuzz.py): python script using an incremental payload to fuzz a remote target;
* [gen-payload.sh](gen-payload.sh): bash script to generate custom payload to exploit simple stack buffer overflows;
* [gen-badchars.py](gen-badchars.py): python script to generate badchars string commonly used for exploiting stack buffer oveflows;
* [ipsweep.sh](ipsweep.sh): bash script that implements a basic IPv4 sweep scan;
* [parse-LaTeX/](parse-LaTeX/): collection of python scripts to parse and clean LaTeX code;
* [portscanner.py](portscanner.py): python script that implements a basic single-thread IPv4 port scanner;
* [pwn-script.py](pwn-script.py): python script that uses pwntools library to exploit simple stack buffer overflows on local or remote targets;
* [Spray-Passwords.ps1](Spray-Passwords.ps1): PowerShell script from [ZilentJack](https://github.com/ZilentJack/Spray-Passwords/blob/master/Spray-Passwords.ps1) to perform password spraying attacks against user accounts in Active Directory (AD) (original source no longer available);
* [smb-ver.sh](smb-ver.sh): bash script for SMB server version enumeration, adapted from [HackTricks.xzy](https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb);
* [verify-PGP.sh](verify-PGP.sh): bash script to verify a PGP-signed messaged against its public key, without permanently import the key;
* [WebRecon.sh](WebRecon.sh): bash script for basic website information gathering;

Please note that these scripts are just helpers I use in my activities and might be (partially) useful for conscious users. I do not consider them a final product ready out-of-the-box, thus, errors and bugs might be present.

Proposed updates/fixes/improvements are always welcome.

# License
These scripts are free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details.

# Copyright

Copyright (C) 2020-2021 Michele De Donno, All Rights Reserved
