##### 
##### Author: Hai-Anh Le
##### Date  : February 2017 
##### Goal  : Generate Graphene sheets given n (n isn't really great)
#####
import numpy
import random
import math
from math import pi # from (library) import (member)

n = int(input("n = "))
ncol = int(n/2)
nC = ((2*n-2)*4+6)*(2*ncol+1)
rCC = 1.42

print("Number of Carbon atoms = ", nC)
print("Number of benzene rings = ", 2*ncol*(2*n-2)+(2*ncol+1)*(2*n-1))

coordinates = []
z = 0.0

#central ring
theta = pi/3.0
Ax = -rCC * math.cos(theta)
Ay =  rCC * math.sin(theta)
coordinates.append("C" + "    " + '%.9f' %Ax + "    " + '%.9f' %Ay + "    " + '%.9f' %z)
Bx = -Ax 
By = Ay
coordinates.append("C" + "    " + '%.9f' %Bx + "    " + '%.9f' %By + "    " + '%.9f' %z)
Cx = rCC
Cy = 0.0
coordinates.append("C" + "    " + '%.9f' %Cx + "    " + '%.9f' %Cy + "    " + '%.9f' %z)
Dx = Bx
Dy = -By
coordinates.append("C" + "    " + '%.9f' %Dx + "    " + '%.9f' %Dy + "    " + '%.9f' %z)
Ex = Ax
Ey = -Ay
coordinates.append("C" + "    " + '%.9f' %Ex + "    " + '%.9f' %Ey + "    " + '%.9f' %z)
Fx = -Cx
Fy = 0.0
coordinates.append("C" + "    " + '%.9f' %Fx + "    " + '%.9f' %Fy + "    " + '%.9f' %z)

###
for j in range(-ncol,ncol+1):
  for i in range(0,n):
    if (i != 0 or j != 0):
      Ax_j = Ax + 3.0*j*rCC
      Ay_i = Ay + 2.0*i*Ay
  
      Bx_j = Bx + 3.0*j*rCC
      By_i = Ay_i
  
      Cx_j = Cx + 3.0*j*rCC
      Cy_i = 2.0*i*By
  
      Fx_j = Fx + 3.0*j*rCC
      Fy_i = Cy_i
      coordinates.append("C" + "    " + '%.9f' %Ax_j + "    " + '%.9f' %Ay_i + "    " + '%.9f' %z)
      coordinates.append("C" + "    " + '%.9f' %Bx_j + "    " + '%.9f' %By_i + "    " + '%.9f' %z)
      coordinates.append("C" + "    " + '%.9f' %Cx_j + "    " + '%.9f' %Cy_i + "    " + '%.9f' %z)
      coordinates.append("C" + "    " + '%.9f' %Fx_j + "    " + '%.9f' %Fy_i + "    " + '%.9f' %z)
  
      Dx_j = Dx - 3.0*j*rCC
      Dy_i = -By_i
  
      Ex_j = Ex - 3.0*j*rCC
      Ey_i = -Ay_i
  
      Cx_j1 = Cx - 3.0*j*rCC
      Cy_i1 = -Cy_i
  
      Fx_j1 = Fx - 3.0*j*rCC
      Fy_i1 = -Fy_i
      coordinates.append("C" + "    " + '%.9f' %Dx_j + "    " + '%.9f' %Dy_i + "    " + '%.9f' %z)
      coordinates.append("C" + "    " + '%.9f' %Ex_j + "    " + '%.9f' %Ey_i + "    " + '%.9f' %z)
      if (i != 0):
        coordinates.append("C" + "    " + '%.9f' %Cx_j1 + "    " + '%.9f' %Cy_i1 + "    " + '%.9f' %z)
        coordinates.append("C" + "    " + '%.9f' %Fx_j1 + "    " + '%.9f' %Fy_i1 + "    " + '%.9f' %z)

## write xyz file
natom = nC
outFile = open("graphene-C" + str(nC) + ".xyz", 'w')
outFile.write(str(natom) + "\n")
outFile.write("Graphene C" + str(nC) + " in xyz format\n")
for point in coordinates:
  outFile.write(point + "\n")

outFile.close()
