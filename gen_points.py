##### 
##### Author: Hai-Anh Le
##### Date  : Feb 20, 2015
##### Goal: Generate N random points in a box of max length a
#####
import numpy
import random


##Parameters
max_box_length = 50.0
max_points     = 30
fileName       = "cube"
#fileName       = "plane"

##Generate poitns
coordinates = []
for i in range(max_points):
  x = random.random() ###return the next random floating point number in the range [0.0, 1.0)
  y = random.random()
  z = random.random()
  x = (x - 0.5) * max_box_length
  #x = 0.0
  y = (y - 0.5) * max_box_length
  z = (z - 0.5) * max_box_length
  coordinates.append([x, y, z])

##Write in xyz format
outFile = open(fileName + ".xyz", 'w')
outFile.write(str(max_points) + "\n")
outFile.write("Random points in a box of max length" + str(max_box_length) + "\n")
for point in coordinates:
  outFile.write("He   " + str("%.9f" % point[0]).rjust(15) + "  " + str("%.9f" % point[1]).rjust(15) + "  " + str("%.9f" % point[2]).rjust(15) + "\n")

outFile.close()


##Write in BAGEL format
outFile = open(fileName + ".json", 'w')
outFile.write("{ \"bagel\" : [\n\n")
outFile.write("{")
outFile.write("  \"title\" : \"molecule\",\n")
outFile.write("  \"symmetry\" : \"C1\",\n")
outFile.write("  \"basis\" : \"svp\",\n")
outFile.write("  \"angstrom\" : \"false\",\n")
outFile.write("  \"geometry\" : [\n")

i = 0
for point in coordinates:
  outFile.write("     { \"atom\" : \"He\",  \"xyz\" : [  ")
  if (i < max_points - 1):
    outFile.write(str("%.9f" % point[0]).rjust(12) + ", " + str("%.9f" % point[1]).rjust(12) + ", " + str("%.9f" % point[2]).rjust(12) + "]},\n")
  else:
    outFile.write(str("%.9f" % point[0]).rjust(12) + ", " + str("%.9f" % point[1]).rjust(12) + ", " + str("%.9f" % point[2]).rjust(12) + "]}\n")
  i += 1

outFile.write("  ]\n")
outFile.write("},\n\n")
outFile.write("{")
outFile.write("  \"title\" : \"hf\",\n")
outFile.write("  \"df\" : \"false\",\n")
outFile.write("  \"thresh\" : 8.0e-10\n")
outFile.write("}\n\n")
outFile.write("]}")
