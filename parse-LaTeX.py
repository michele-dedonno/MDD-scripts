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


# % ======================= DESCRIPTION AND USAGE ======================= &
#
# Script that removes duplicated references in a LaTeX table with a 
# '\multirow{}' cell. Requires an 'input.txt' file in the cwd.
#
# Input:
#   - 'input.txt": file containing the LaTeX code for the table that needs 
#                  to be cleaned.
# Output:
#   - LaTeX string containing the unique references included in the first 
#     '\multirow{}' cell of the table that are NOT referenced anywhere else 
#     in the table


def getList1(data):
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

def getList2(data):
    retlist = []
    searchS = "\cite{"
    # start the string after '\cite{'
    data = data[data.find(searchS)+len(searchS):]
    # end the string before '}'
    data = data[:data.find("}")]
    # split based on ","
    retlist = data.split(",")
    # sort, remove duplicated and blank spaces
    retlist = list(dict.fromkeys(sorted(i.strip() for i in retlist)))
    #print (list2)
    return retlist

# % ================================================================== %
#   Additional function that returns the list of unique references in a 
#   given LaTeX file and their number.
# % ================================================================== %
def uniqueRef(filename):
    f = open(filename)
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

# % =================================================== %
#   Main function
# % =================================================== %
if __name__ == "__main__":
    # Loading data from file
    f = open('input.txt')
    data = f.read()
    f.close()
 
    # % --- Remove the '\cite' in '\multirow' from the data ---%
    #   N.B. only the first '\cite' inside '\multirow' will be processed
    # identify multirow
    searchS = "\multirow{"
    data2 = data[data.find(searchS):]
    searchS = "\cite{"
    # move to '\cite{'
    data2 = data2[data2.find(searchS):]
    # end the string after '}'
    data2 = data2[:data2.find("}")+1]
    data1 = data.replace(data2,"")
    # % --- --- --- --- --- --- --- --- --- --- --- --- ---%

#    print ("Raw input:")
#    print (data)
#    print ("###")
#    print (data1)
#    print ("###")
    print ("Content of \multirow:")
    print (data2)
    print ("###")
    
    # Generate the two lists
    list2 = getList2(data2)
    list1 = getList1(data1)

    # list2 - list1
    result = sorted(list(set(list2)-set(list1)))

    # Intersection between list2 and list2
    removed = sorted(list(set(list2)&set(list1)))
    
    print ("Item removed:")
    print(removed)
    print ("###")
    
    # Print output LaTeX string
    print ("Final string:")
    print("\cite{", end="")
    for i in result:
        print("{}".format(i), end="")
        if i != result[len(result)-1]:
            print(",", end=" ")
    print("}", end="")
    
    # uniqueRef('statistics.txt')
    exit()
