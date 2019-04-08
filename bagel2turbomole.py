##### 
##### Author: Hai-Anh Le
##### Date  : May 28, 2015
#####
import numpy as np

## read json file
fileName = input("BAGEL file name: ")
inFile = open("./" + fileName, 'r')
coordinates = []
natom = 0
for line in inFile.readlines():
  if ("atom" in line):
    natom = natom + 1
    values = line.split()
    atomparts = values[3].split("\"")
    atom = atomparts[1]
    x_tmp = values[7].split(",")
    x = x_tmp[0]
    y_tmp = values[8].split(",")
    y = y_tmp[0]
    z_tmp = values[9].split("]")
    z = z_tmp[0]
    coordinates.append('%.9f' %float(x) + "    " + '%.9f' %float(y) + "    " + '%.9f' %float(z) + "       " + atom.lower())
inFile.close()

## write xyz file
stem = fileName.split(".")
outFile = open("coord", 'w')
outFile.write("$coord\n")
for point in coordinates:
  outFile.write(point + "\n")
outFile.write("$user-defined bonds\n")
outFile.write("$end\n")

outFile.close()

