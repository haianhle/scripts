##### 
##### Author: Hai-Anh Le
##### Date  : April 2016
##### Goal: Generate ideal geometry for polyacetylene of the form H-(C2H2)n-H
#####
import numpy
import random
import math
#from math import pi # from (library) import (member)

##Parameters
n = int(input("H-(C2H2)n-H with n = "))
natom = 2 + 4 * n 

## bond lenghts from JMS 487, 39 (1999) in Angstrom except CH
rC_single = 1.4314
rC_double = 1.3697
angCCC = float(122)/180 * math.pi
rCC = math.sqrt(rC_single**2 + rC_double**2 - 2*rC_single*rC_double*math.cos(angCCC))
rCH = 1.1 
alpha = math.acos((rC_double**2 + rCC**2 - rC_single**2)/(2*rCC * rC_double))

##Generate coordinates
coordinates = []
z = 0.0 ##planar

##H0
theta = math.pi/2 - alpha
phi = math.pi - 2*theta
H0y = -1.0 * math.cos(phi) * rCH
H0x = -1.0 * math.sin(phi) * rCH 
coordinates.append("H" + "    " + '%.9f' %H0x + "    " + '%.9f' %H0y + "    " + '%.9f' %z)

##(C2H2)n backbone
for i in range(0,n):
  C1y = 0.0
  C1x = rCC*i
  coordinates.append("C" + "    " + '%.9f' %C1x + "    " + '%.9f' %C1y + "    " + '%.9f' %z)
  
  H1y = rCH
  H1x = C1x
  coordinates.append("H" + "    " + '%.9f' %H1x + "    " + '%.9f' %H1y + "    " + '%.9f' %z)

  C2y = -1.0 * math.sin(alpha)*rC_double
    ##check1 = math.sin(alpha)*rC_double * rCC
    ##check2 = rC_double*rC_single*math.sin(angCCC)
    ##print str(check1) + "  should be same as    " + str(check2)
  C2x = C1x + math.cos(alpha)*rC_double
  coordinates.append("C" + "    " + '%.9f' %C2x + "    " + '%.9f' %C2y + "    " + '%.9f' %z)

  H2y = C2y - rCH
  H2x = C2x
  coordinates.append("H" + "    " + '%.9f' %H2x + "    " + '%.9f' %H2y + "    " + '%.9f' %z)

  if (i == n-1):
    Hny = C2y - H0y
    Hnx = C2x - H0x ##math.sin(phi) * rCH 
    coordinates.append("H" + "    " + '%.9f' %Hnx + "    " + '%.9f' %Hny + "    " + '%.9f' %z)
    
  
## write xyz file to standard output
stem = "C" + str(2*n) + "H" + str(2*n+2)
outFile = open(stem + ".xyz", 'w')
outFile.write(str(natom) + "\n")
outFile.write("Geometry H-(C2H2)n-H in xyz format\n")
for point in coordinates:
  outFile.write(point + "\n")
outFile.close()
