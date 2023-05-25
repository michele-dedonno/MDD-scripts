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
#     PowerShell script that keeps your computer awake by programmatically 
#     pressing the ScrollLock key every X seconds.
#
#     Last modification date: 12-04-2021
#
#     Example of usage:
#		  powershell.exe -c ".\NoSleep.ps1" 
#
#     This script is inspired from: https://gist.github.com/MatthewSteeples/ce7114b4d3488fc49b6a
#   % ====================================================================== %



############# TO EDIT #############
param($sleep = 240) # seconds
$announcementInterval = 5 # loops
###################################
$announcSecs = $sleep * $announcementInterval #secs

# Clear the display in the host program
Clear-Host

$WShell = New-Object -com "Wscript.Shell"
$date = Get-Date -Format "dddd MM/dd HH:mm (K)"

# Start stopwatch for the elapsed time announcement
$stopwatch
# Some environments don't support invocation of this method.
try {
    $stopwatch = [system.diagnostics.stopwatch]::StartNew()
} catch {
   Write-Host "Couldn't start the stopwatch."
}

Write-Host "******************************************************"
Write-Host "Executing ScrollLock-toggle NoSleep routine."
Write-Host "Start time:" $(Get-Date -Format "dddd MM/dd HH:mm (K)")
Write-Host "------------------------------------------------------"
Write-Host "ScrollLock key press interval:`t $sleep seconds"
Write-Host "Announcement Interval:`t`t $announcSecs seconds"
Write-Host "------------------------------------------------------"

$index = 0
while ( $true )
{	
	# Heartbeat + Press "ScrollLock"
    Write-Host "< 3" -fore red
    $WShell.sendkeys("{SCROLLLOCK}")
    Start-Sleep -Milliseconds 200
    $WShell.sendkeys("{SCROLLLOCK}")
    Write-Host "<3" -fore red
	
	# Sleep
    Start-Sleep -Seconds $sleep

    # Announce runtime every announcementInterval loops
    if ( $stopwatch.IsRunning -and (++$index % $announcementInterval) -eq 0 )
    {
       Write-Host "Elapsed time: " $stopwatch.Elapsed.ToString('dd\.hh\:mm\:ss') "(dd.hh:mm:ss)"
    }
}
