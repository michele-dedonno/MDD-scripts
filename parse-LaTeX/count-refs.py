#!/usr/bin/env python
# coding: utf-8

# Copyright (C) 2020 Michele De Donno

# % ============================== LICENSE ============================== %
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
# % ====================================================================== %


# % ======================= DESCRIPTION AND USAGE ======================= %
#   Copy all the LaTeX text you want to analyze (e.g., section, subection, 
#   table) in the "statistics.txt".
#   This script will return the list of (unique) references in the file and
#   their number.
# % ====================================================================== %

f = open('statistics.txt')
data = f.read()
f.close()
retlist = []
searchS = "\cite{"
found = data.find(searchS)
while(found != -1):
    # start the string after '\cite{'
    data = data[found+len(searchS):]
    # remove everything after the final bracets and generate the list
    temp = data[:data.find("}")]
    retlist += temp.split(",")
    # process the next substring
    found = data.find(searchS)
# sort, remove duplicated and blank spaces
result = list(dict.fromkeys(sorted(i.strip() for i in retlist)))

# Print output
print("\cite{", end="")
for i in result:
    if i != result[len(result)-1]:
        print("{}".format(i), end=", ")
    else:
        print("{}".format(i), end="")
print("}")
print("###")
print("Number of elements: {}".format(str(len(result))))
