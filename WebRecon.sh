#!/bin/bash

#   Copyright (C) 2021 Michele De Donno

#   % ============================== LICENSE ============================== %
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>
#   % ====================================================================== %


#   % ======================= DESCRIPTION AND USAGE ======================= &
#     Bash script that implements a basic Web Application enumerations of 
#     the target domain provided as input.
#
#     Requirements
#	  	This script uses the following tools for enumerating the target:
#			- assetfinder (https://github.com/tomnomnom/assetfinder)
#			- amass (https://github.com/OWASP/Amass)
#			- httprobe (https://github.com/tomnomnom/httprobe)
#			- gowitness (https://github.com/sensepost/gowitness)
#		Please make sure to install these tools before running the script.
#
#     Example of usage:
#		$ ./WebRecon.sh hackme.com
#
#     This script is inspired from the Udemy course "Practical Ethical 
#     Hacking - The Complete Course" taught by Heath Adams.
#   % ====================================================================== %
#


# Variables
target=${1}
output=${target}/recon

# Usage
if [ "${1}" == "" ]
then
	echo -e "Error:\t Missing target domain.";
	echo -e "Usage:\t $0 <target-domain>. Example: $0 hackme.com";
	exit 1;
fi

# Create output folder
mkdir -p ${output}

# Find target subdomains and related assets with assetfinder
echo "[+] Harvesting subdomains and assets for target domain '${target}' using 'assetfinder'"
assetfinder ${target} > ${output}/assets.txt
if [ $? -eq 0 ]; then
	echo "[+] Full assetfinder output available at ${output}/assets.txt"
	# Extract sub-domains only
	cat ${output}/assets.txt | grep ${target} > ${output}/subdomains.txt
	if [ $? -eq 0 ]; then
		echo "[+] Filtered output available at ${output}/subdomains.txt"
		# removing duplicates
 		sort -u -o ${output}/subdomains.txt{,}
 		if [ $? -ne 0 ]; then
 			echo "[-] Failed to sort ${output}/subdomains.txt"
 		fi
 	else
 	   	echo "[-] ERROR, skipping filtering of subdomains"
	fi
else
	echo "[-] ERROR, skipping harvesting with assetfinder"
fi

# Find target subdomains and related assets with amass
echo "[+] Harvesting subdomains and assets for target domain '${target}' using 'Amass'"
amass enum -d ${target} >> ${output}/subdomains.txt
if [ $? -eq 0 ]; then
	echo "[+] Amass output added to ${output}/subdomains.txt"
	# removing duplicates
	sort -u -o ${output}/subdomains.txt{,}
	if [ $? -ne 0 ]; then
		echo "[-] Failed to sort ${output}/subdomains.txt"
	fi
else
	echo "[-] ERROR, skipping harvesting with Amass"
fi

# Probe for working http and https servers
echo "[+] Probing for alive domains (over http and https) using 'httprobe'"
cat ${output}/subdomains.txt | httprobe | awk -F '//' '{print $2}' | tr -d ':*' >> ${output}/alive-subdomains.txt
if [ $? -eq 0 ]; then
	echo "[+] Alive subdomains available at ${output}/alive-subdomains.txt"
else
	echo "[-] ERROR, skipping probing with httprobe"
fi

# Take a screenshot of all alive domains
echo "[+] Taking screenshots of alive domains using 'eyewitness'"
mkdir -p ${output}/screenshots
gowitness file -f ${output}/alive-subdomains.txt -P ${output}/screenshots
if [ $? -eq 0 ]; then
	echo "[+] Screenshots available at ${output}/screenshots"
else
	echo "[-] ERROR, skipping screenshots with gowitness"
fi
