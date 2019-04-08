##### 
##### Author: Hai-Anh Le
##### Date  : April 2016
##### Goal: Generate ideal geometry for alkanes of the form C2nH4n+2
#####
import numpy
import random
import math
from math import pi # from (library) import (member)

##Parameters
n = int(input("Alkanes H-(C2H4)n-H with n = "))
natom = 2 + 6 * n 

## bond lenghts in angstrom and angles https://en.wikipedia.org/wiki/Bond_length
rCC = 1.54
rCH = 1.10
aHCH = 109.5/180.0 * pi
aHCH_half = 0.5 * aHCH
aCCC = 109.5/180.0 * pi
dCC = math.sqrt(2 * rCC**2 * (1 - math.cos(aCCC))) #C1 and C1 of next unit
alpha = 0.5 * (pi - aCCC)
theta = 0.5 * (pi - aHCH)

##Generate coordinates
##All C atoms on xy plane
Cz = 0.0
coordinates = []

### First H attached to C1
H0z = 0.0
H0y = rCH * math.sin(theta)
H0x = -1.0 * rCH * math.cos(theta)
coordinates.append("H" + "    " + '%.9f' %H0x + "    " + '%.9f' %H0y + "    " + '%.9f' %H0z)
    
###(C2H4)n backbone
for i in range(0,n):
  C1y = 0.0
  C1x = dCC*i
  coordinates.append("C" + "    " + '%.9f' %C1x + "    " + '%.9f' %C1y + "    " + '%.9f' %Cz)
 
  H1x = C1x
  H1az = rCH * math.sin(aHCH_half)
  H1ay = -1.0 * rCH * math.cos(aHCH_half)
  coordinates.append("H" + "    " + '%.9f' %H1x + "    " + '%.9f' %H1ay + "    " + '%.9f' %H1az)

  H1bz = -1.0 * H1az
  H1by = H1ay
  coordinates.append("H" + "    " + '%.9f' %H1x + "    " + '%.9f' %H1by + "    " + '%.9f' %H1bz)

  C2y =  rCC * math.sin(alpha)
  C2x =  C1x + 0.5*dCC
  coordinates.append("C" + "    " + '%.9f' %C2x + "    " + '%.9f' %C2y + "    " + '%.9f' %Cz)
  
  H2x = C2x
  H2az = H1az
  H2ay = C2y + rCH * math.cos(aHCH_half)
  coordinates.append("H" + "    " + '%.9f' %H2x + "    " + '%.9f' %H2ay + "    " + '%.9f' %H2az)

  H2bz = H1bz
  H2by = H2ay
  coordinates.append("H" + "    " + '%.9f' %H2x + "    " + '%.9f' %H2by + "    " + '%.9f' %H2bz)

  if (i == n-1):
    Hnz = 0.0
    Hny = C2y - rCH * math.sin(theta)
    Hnx = C2x + rCH * math.cos(theta)
    coordinates.append("H" + "    " + '%.9f' %Hnx + "    " + '%.9f' %Hny + "    " + '%.9f' %Hnz)
  
## write xyz file to standard output
stem = "C" + str(2*n) + "H" + str(4*n+2)
outFile = open(stem + ".xyz", 'w')
outFile.write(str(natom) + "\n")
outFile.write("Geometry H-(C2H4)n-H in xyz format\n")
for point in coordinates:
  outFile.write(point + "\n")
outFile.close()
