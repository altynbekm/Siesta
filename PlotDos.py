#!/usr/bin/python
from numpy import *
#from scipy import *
#import array
import os		#next two lines helps me to run commandline agument in python
import sys
#import operator #use with the operator sorted
from operator import itemgetter
##########################################################################
#
#USAGE: ./EXECUTABLE
# you need a file which contains the the ELEMENT POSITION
# change the name of EMPDOS
##########################################################################
if len(sys.argv) != 2:
        print '\n\nUsage: %s database \n ###IMPORTANT DETAIL: Name of PDOS file###\n' % (sys.argv[0])
        sys.exit(1)

dosfile = open(sys.argv[1], "r")
array0 = []
array1 = []

for line in dosfile:
	aa = line.strip().split()
	array0.append(aa[:2])
#	array0.append(aa[2:])

dosfile.close()

lengthOfFile=len(array0)
#print(lengthOfFile)
#print array0[6][1]
#print array0[4][1]

user_name = 'folder'
#mater="C"
mater = raw_input("Enter the element whose pdos you want:  \n  ")
EMPDOS = raw_input("Enter the name of the PDOS file:  \n  ")
for n in range(0, lengthOfFile):
	element = array0[n][0]
	elementNum = array0[n][1]
        if element == mater:
                fileName = "%s%d" % (element, n)
		print fileName
	#	os.system("mkdir pdos")
		File="pdos-"+fileName+".txt"
		fout=open(File,"w")
		fout.write(EMPDOS)
		fout.write("\n")
		fout.write("1\n")
		fout.write(elementNum)
                fout.close()
		os.system("~/bin/pdos-siesta.exe < "+File)
		os.system("mkdir pdos-"+fileName)
		os.system("mv "+File+" pdos-"+fileName)
		os.system("mv pdos_*.dat pdos-"+fileName)



count_elem = 0
for n in range(0, lengthOfFile):
	element = array0[n][0]
	if element == mater:
		count_elem = count_elem +  1
                print count_elem

print count_elem


EleName = "Total-"+mater
File="pdos-"+EleName+".txt"
fout=open(File,"w")
fout.write(EMPDOS)
fout.write("\n")
count_elem = str(count_elem)
fout.write( count_elem )

#print cout_element
print EleName




for n in range(0, lengthOfFile):
	element = array0[n][0]
	elementNum = array0[n][1]
	if element == mater:
                fout.write("\n")
		fout.write(elementNum)
#		os.system("mkdir "+fileName)

fout.close()
os.system("~/bin/pdos-siesta.exe < "+File)
os.system("mkdir "+EleName)
os.system("mv "+File+" "+EleName)
os.system("mv pdos_*.dat "+EleName)
