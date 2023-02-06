#    Copyright (C) 2023 Michele De Donno

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
#     PowerShell script that lists Service Principal Names (SPNs) of 
#     all non-disabled user objects.
#
#     Example of usage:
#     .\List-SPNs.ps1 > SPNs.txt
#     powershell.exe -exec bypass -command ".\List-SPNs.ps1 > SPNs.txt" 
#
#   % ====================================================================== %
#
#

<# Initialization #>
try {
	# Instantiation of the DirectorySearch class for the entire AD
	$Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]"")
} catch {
	Write-Error "$_.Exception.Message" -ErrorAction Stop
	#$_.Exception.Message
	#Exit
}

<# LDAP Query #>
$Searcher.filter="(&(samAccountType=805306368)(servicePrincipalName=*)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))" # all user objects, not disabled accounts
# $Searcher.filter="serviceprincipalname=*http*" # web servers
# $Searcher.filter="(servicePrincipalName=*)" # all SPNs - note: LDAP results are limited, so you might miss some SPNs

<# Parse result and format output #>
$spnsList = New-Object -TypeName 'System.Collections.ArrayList';
$services = $Searcher.FindAll()
# to filter:
# $services = $Searcher.FindAll() | ?{ $_.path -like '*OU=whatever,DC=whatever,DC=whatever*' }

Foreach($obj in $services)
{
	$entry = $obj.GetDirectoryEntry()
	#$output = "Object Name = "+$entry.name
	#Write-Output $output
	#$output = "DN = "+$entry.distinguishedName
	#Write-Output $output
	#$output = "Object Category = "+$entry.objectCategory
	#Write-Output "Service Principal Names:"
	foreach($SPN in $entry.servicePrincipalName) {
		$index = $spnsList.Add($SPN)
		#$SPN
	}
	#Write-Output "--------------"
}
$spnsList | sort -uniq
