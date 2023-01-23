#!/bin/bash

#   Copyright (C) 2023 Michele De Donno

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
#    Bash script to setup the ftpd after first installation
#
#     Example of usage:
#		  $ sudo ./setup-ftpd.sh 
#
#     This script is inspired from the Offensive Security course "PEN-200"
#   % ====================================================================== %
#

# ============= EDIT THIS VALUES BEFORE RUNNING  ============= #
sgroup=ftpgroup
suser=kali-ftp
ftpuser=kaliftpd
ftphome=/ftphome
# ============ ============ ============ ============ ======== #

echo "[+] configuring FTPd server using the following data.";
echo "[>] OS user: $suser"
echo "[>] OS group: $sgroup"
echo "[>] FTPd user: $ftpuser"
echo "[>] FTPd user home: $ftphome"

# create ftpgroup
groupadd $sgroup
# create new sytem user
echo "[*] Setting up the FTP user '$ftpuser'."
useradd -g $sgroup -d /dev/null -s /etc $suser
# configure Pure-FTPd
pure-pw useradd $ftpuser -u $suser -d $ftphome
pure-pw mkdb
cd /etc/pure-ftpd/auth/
ln -s ../conf/PureDB 60pdb
mkdir -p $ftphome
chown -R $suser:$sgroup $ftphome
systemctl restart pure-ftpd

echo "[+] Finished."
