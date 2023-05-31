#!/bin/python3

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
#     Python script that keeps your computer awake by programmatically 
#     pressing the CTRL key every X seconds.
#
#
#     Usage:
#	      sudo pip install keyboard		
#	      sudo python3 NoSleep.py
#
#   % ====================================================================== %

import time, keyboard
from datetime import datetime

############# TO EDIT #############
sleeptime = 4 * 60 # seconds
###################################

while True:
	keyboard.send("CTRL")
	print("< 3")
	time.sleep(sleeptime)
	print("<3")
