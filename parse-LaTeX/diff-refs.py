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

# % ============================== Description ============================== %
#   This script will return all (unique) references in "statistics.txt" which are 
#   not in "toremove.txt", i.e., "statistics.txt"-"toremove.txt"
# % ============================== =========== ============================== %


# return a list containing all the cited (unique) elements in "data"
def getList(data):
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
    retlist = list(dict.fromkeys(sorted(i.strip() for i in retlist)))
    #print (list)
    return retlist

if __name__ == "__main__":
    # Loading data from files
    f = open('statistics.txt')
    data1 = f.read()
    f.close()
    f = open('toremove.txt')
    data2 = f.read()
    f.close()

  
    # Generate the two lists
    list1 = getList(data1)
    list2 = getList(data2)

    # list1 - list2
    result = sorted(list(set(list1)-set(list2)))

    # Intersection between list1 and list2
    removed = sorted(list(set(list1)&set(list2)))
    
    print ("Item removed: "+str(len(removed)))
    print (removed)
    print ("###")
    
    # Print output LaTeX string of unique references
    print ("Unique string ("+str(len(result))+" elements):")
    print("\cite{", end="")
    for i in result:
        print("{}".format(i), end="")
        if i != result[len(result)-1]:
            print(",", end=" ")
    print("}", end="")
