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
#   Input: 2 columns table copied directly from google sheet
#   Output: 5 columns LaTeX table
# % ====================================================================== %

def fillLists(data):
    for line in data:
        ID,perc = line.split("	")
        n = float(perc[:len(perc)-1])
        if n > 4:
            vhigh.append(line)
        elif n <=4 and n>2.5:
            high.append(line)
        elif n <=2.5 and n>1:
            medium.append(line)
        elif n <=1:
            low.append(line)
            
def printList(mlist):
    for j in mlist:
        ID,perc = j.split("	")
        temp = ID[:2]
        cat = switcher1.get(temp)
        req = switcher2.get(ID.strip())
        perc = round(float(perc[:len(perc)-1]),1)
        if j != mlist[len(mlist)-1]:
            print("& "+str(ID)+" & "+str(req)+" & "+str(cat)+" & "+str(perc)+ "\% \\\ ")
        else:
            print("& "+str(ID)+" & "+str(req)+" & "+str(cat)+" & "+str(perc)+ "\% \\\ \hline") 

if __name__ == "__main__":
    switcher1={
        'A-':'Authentication',
        'AC':'Access Control',
        'M-':'Maintainability',
        'R-':'Resilience',
        'DS':'Data Security and Data Sharing',
        'SM':'Security Monitoring',
        'NS':'Network Security',
        'MM':'Models and Methodologies'
    }
    switcher2={
        'A-01':'multi-factor authentication',
        'A-02':'key distribution',
        'A-03':'node addition, revocation, rekeying',
        'A-04':'decentralized key management',
        'A-05':'transitive authentication',
        'A-06':'mutual authentication',
        'A-07':'privacy-preserving authentication',
        'A-08':'minimization of user interaction',
        'A-09':'non-repudation',
        'A-10':'attestation',
        'AC-01':'handle dynamic changes',
        'AC-02':'fine-grained \\ac{AC}',
        'AC-03':'centralized \\ac{AC}',
        'AC-04':'decentralized \\ac{AC}',
        'AC-05':'privacy-preserving \\ac{AC}',
        'AC-06':'transparency',
        'AC-07':'compatibility',
        'M-01':'software updateability',
        'M-02':'configuration updateability',
        'M-03':'disturbance-free updates',
        'M-04':'usability of update process',
        'M-05':'traceability',
        'M-06':'compatibility',
        'M-07':'transparency',
        'M-08':'secure status transfer',
        'R-01':'continuation of operation with compromised subsystems',
        'R-02':'operation with intermittent connectivity',
        'R-03':'standards compliance',
        'DSS-01':'data loss mitigation',
        'DSS-02':'data confidentiality',
        'DSS-03':'standardization',
        'DSS-04':'secure data transport',
        'DSS-05':'secure external data storage',
        'DSS-06':'data flow control',
        'DSS-07':'data protection legislation compliance',
        'SM-01':'infrastructure monitoring',
        'SM-02':'threat response',
        'SM-03':'handle heterogeneous sources',
        'SM-04':'security policy enforcement',
        'NS-01':'dynamicity of configuration',
        'NS-02':'security policy enforcement',
        'NS-03':'management overhead minimization',
        'NS-04':'network isolation',
        'NS-05':'timeliness',
        'NS-06':'availability  (\\ac{DoS}, jamming, etc.)',
        'NS-07':'wireless transmission security',
        'MM-01':'adequate risk/threat assessment',
        'MM-02':'minimization of overall attack surface',
        'MM-03':'security by design'
    }
    
    vhigh = list()
    high = list()
    medium = list()
    low = list()
    
    f = open('statistics.txt')
    data = f.read()
    f.close()
    
    rows = data.split("\n")
    
    # Split rows based on interest level
    fillLists(rows)
    
    # Print lists
    print("\multirow{"+str(len(vhigh))+"}{*}{Very High}", end=" ")
    printList(vhigh)
    print("\multirow{"+str(len(high))+"}{*}{High}", end=" ")
    printList(high)
    print("\multirow{"+str(len(medium))+"}{*}{Medium}", end=" ")
    printList(medium)
    print("\multirow{"+str(len(low))+"}{*}{Low}", end=" ")
    printList(low)
