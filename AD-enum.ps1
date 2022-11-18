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
#     PowerShell script that implements basic Active Directory enumeration
#     when executed on a domain-joined machine.
#
#     Example of usage:
#		  powershell.exe -exec bypass -command ".\AD-enum.ps1" 
#
#     This script is inspired from the Offensive Security course "PEN-200 | PWK"
#   % ====================================================================== %
#
#

# $domainObj: Entire domain object
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
# $PDC: Name of the Primary Domain Controller (PDC)
$PDC = ($domainObj.PdcRoleOwner).Name
# $SearchString: LDAP provider path to perform LDAP query against the DC
$SearchString = "LDAP://"
$SearchString += $PDC + "/"
$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
$SearchString += $DistinguishedName
$output="Search String: "+$SearchString
$output
# N.B. the DistinguishedName will consist of the domain name ("corp.com") broken down into individual domain components (DC) (“DC=corp,DC=com”)

# Instantiation of the DirectorySearch class
$Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
$objDomain = New-Object System.DirectoryServices.DirectoryEntry
# SearchRoot with no constructure will return results from the entire AD
$Searcher.SearchRoot = $objDomain

# Users
$Searcher.filter="samAccountType=805306368" # all users in the domain
# $Searcher.filter="name=Jeff_Admin" # search for a specific domain user
$users = $Searcher.FindAll()
# output for users listing
Write-Host "########## Users ##########"
Foreach($obj in $users)
{
 Foreach($prop in $obj.Properties)
 {
  $prop
 }

 Write-Host "------------------------"
}

# Groups and related members
$Searcher.filter="(objectClass=Group)" # all groups in the domain
# $Searcher.filter="(name=Secret_Group)" # search for a specific group
$groups = $Searcher.FindAll()
Write-Host "########## Groups ##########"
Foreach($obj in $groups)
{
  Write-Host "Group:" 
  $obj.Properties.name
  Write-Host "Members:" 
  $obj.Properties.member
  Write-Host "------------------------"
}

# Service Principal Names
$Searcher.filter="serviceprincipalname=*"
# $Searcher.filter="serviceprincipalname=*http*" # web servers
$services = $Searcher.FindAll()
Write-Host "########## Services ##########"
Foreach($obj in $services)
{
 Foreach($prop in $obj.Properties)
 {
  $prop
  Write-Host "DNS Lookup:"
  # try {
    # $addresses = [System.Net.Dns]::GetHostAddresses("$prop.dnshostname").IPAddressToString
  # }
  # catch { 
    # $addresses = "Server IP cannot resolve."
  # }
  # foreach($address in $addresses) {
    # Write-Host $dnshost, $address 
  # }
  nslookup $prop.dnshostname
  #(nslookup $prop.dnshostname | Select-String Address | Where-Object LineNumber -eq 5).ToString().Split(' ')[-1]
 }

 Write-Host "------------------------"
}
