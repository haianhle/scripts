##### 
##### Author: Hai-Anh Le
##### Date  : February 2017 
##### Goal  : Generate circular shaped H-Graphene C_{6n^2}H_{6n} given n
#####
import numpy
import random
import math
from math import pi # from (library) import (member)

n = int(input("n = "))

nC = 6*n*n
nH = 6*n
rCC = 1.42
rCH = 1.08
ncol = int(n/2)

n_is_odd = False
if (ncol*2 != n):
  n_is_odd = True

print("Number of Carbon atoms = ", nC)
print("Number of Hydrogen atoms = ", nH)
print("Number of benzene rings = ", (3*n-2)*(n-1)+2*n-1)

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
  for i in range(0,n-abs(j)):
    if (i != 0 or j != 0):
      Ax_j = Ax + 3.0*j*rCC
      Ay_i = Ay + 2.0*i*Ay
      Bx_j = Bx + 3.0*j*rCC
      By_i = Ay_i
      Cx_j = Cx + 3.0*j*rCC
      Cy_i = 2.0*i*By
      Fx_j = Fx + 3.0*j*rCC
      Fy_i = Cy_i
      Dx_j = Dx - 3.0*j*rCC
      Dy_i = -By_i
      Ex_j = Ex - 3.0*j*rCC
      Ey_i = -Ay_i
      Cx_j1 = Cx - 3.0*j*rCC
      Cy_i1 = -Cy_i
      Fx_j1 = Fx - 3.0*j*rCC
      Fy_i1 = -Fy_i

      if (n_is_odd == True or j != ncol):
        coordinates.append("C" + "    " + '%.9f' %Bx_j + "    " + '%.9f' %By_i + "    " + '%.9f' %z)
        coordinates.append("C" + "    " + '%.9f' %Cx_j + "    " + '%.9f' %Cy_i + "    " + '%.9f' %z)
        coordinates.append("C" + "    " + '%.9f' %Ex_j + "    " + '%.9f' %Ey_i + "    " + '%.9f' %z)
        if (i != 0):
          coordinates.append("C" + "    " + '%.9f' %Fx_j1 + "    " + '%.9f' %Fy_i1 + "    " + '%.9f' %z)

      if (n_is_odd == True or j != -ncol):
        coordinates.append("C" + "    " + '%.9f' %Ax_j + "    " + '%.9f' %Ay_i + "    " + '%.9f' %z)
        coordinates.append("C" + "    " + '%.9f' %Fx_j + "    " + '%.9f' %Fy_i + "    " + '%.9f' %z)
        coordinates.append("C" + "    " + '%.9f' %Dx_j + "    " + '%.9f' %Dy_i + "    " + '%.9f' %z)
        if (i != 0):
          coordinates.append("C" + "    " + '%.9f' %Cx_j1 + "    " + '%.9f' %Cy_i1 + "    " + '%.9f' %z)

  
      if (i == n-abs(j)-1 and j > 0):
        Fy_i2 = 2.0*(i+1)*By
        Fy_i3 = -Fy_i2
        coordinates.append("C" + "    " + '%.9f' %Fx_j + "    " + '%.9f' %Fy_i2 + "    " + '%.9f' %z)
        coordinates.append("C" + "    " + '%.9f' %Fx_j + "    " + '%.9f' %Fy_i3 + "    " + '%.9f' %z)

      if (i == n-abs(j)-1 and j < 0):
        Cy_i2 = 2.0*(i+1)*By
        Cy_i3 = -Cy_i2
        coordinates.append("C" + "    " + '%.9f' %Cx_j + "    " + '%.9f' %Cy_i2 + "    " + '%.9f' %z)
        coordinates.append("C" + "    " + '%.9f' %Cx_j + "    " + '%.9f' %Cy_i3 + "    " + '%.9f' %z)

### Add hydrogen
for j in range(0,ncol+1):
  i = n-abs(j)-1
  Bx_j = Bx + 3.0*j*rCC
  HBx = Bx_j + rCH*math.cos(theta)
  By_i = Ay + 2.0*i*Ay
  HBy = By_i + rCH*math.sin(theta) 
  if (n_is_odd == True or j != ncol):
    #coordinates.append("S" + "    " + '%.9f' %Bx_j + "    " + '%.9f' %By_i + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HBx + "    " + '%.9f' %HBy + "    " + '%.9f' %z)

  Ex_j = Ex - 3.0*j*rCC
  Ey_i =  -Ay - 2.0*i*Ay
  HEx = Ex_j - rCH*math.cos(theta)
  HEy = Ey_i - rCH*math.sin(theta)
  if (n_is_odd == True or j != ncol):
    #coordinates.append("Cl" + "    " + '%.9f' %Ex_j + "    " + '%.9f' %Ey_i + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HEx + "    " + '%.9f' %HEy + "    " + '%.9f' %z)

  Fx_j = Fx + 3.0*j*rCC
  if (j > 0):
    Fy_i2 = 2.0*(i+1)*By
    HFx2 = Fx_j + rCH*math.cos(theta)
    HFy2 = Fy_i2 + rCH*math.sin(theta)
    #coordinates.append("Br" + "    " + '%.9f' %Fx_j + "    " + '%.9f' %Fy_i2 + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HFx2 + "    " + '%.9f' %HFy2 + "    " + '%.9f' %z)
    Fy_i3 = -Fy_i2
    HFx3 = Fx_j + rCH*math.cos(theta)
    HFy3 = Fy_i3 - rCH*math.sin(theta)
    #coordinates.append("Cl" + "    " + '%.9f' %Fx_j + "    " + '%.9f' %Fy_i3 + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HFx3 + "    " + '%.9f' %HFy3 + "    " + '%.9f' %z)

for j in range(-ncol,1):
  i = n-abs(j)-1
  Ax_j = Ax + 3.0*j*rCC
  Ay_i = Ay + 2.0*i*Ay
  HAx = Ax_j - rCH*math.cos(theta)
  HAy = Ay_i + rCH*math.sin(theta) 
  if (n_is_odd == True or j != -ncol):
    #coordinates.append("S" + "    " + '%.9f' %Ax_j + "    " + '%.9f' %Ay_i + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HAx + "    " + '%.9f' %HAy + "    " + '%.9f' %z)

  Dx_j = Dx - 3.0*j*rCC
  Dy_i = -Ay - 2.0*i*Ay
  HDx = Dx_j + rCH*math.cos(theta)
  HDy = Dy_i - rCH*math.sin(theta)
  if (n_is_odd == True or j != -ncol):
    #coordinates.append("Cl" + "    " + '%.9f' %Dx_j + "    " + '%.9f' %Dy_i + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HDx + "    " + '%.9f' %HDy + "    " + '%.9f' %z)

  Cx_j = Cx + 3.0*j*rCC
  if (j < 0):
    Cy_i2 = 2.0*(i+1)*By
    HCx2 = Cx_j - rCH*math.cos(theta)
    HCy2 = Cy_i2 + rCH*math.sin(theta)
    #coordinates.append("Cl" + "    " + '%.9f' %Cx_j + "    " + '%.9f' %Cy_i2 + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HCx2 + "    " + '%.9f' %HCy2 + "    " + '%.9f' %z)
    Cy_i3 = -Cy_i2
    HCx3 = Cx_j - rCH*math.cos(theta)
    HCy3 = Cy_i3 - rCH*math.sin(theta)
    #coordinates.append("Br" + "    " + '%.9f' %Cx_j + "    " + '%.9f' %Cy_i3 + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HCx3 + "    " + '%.9f' %HCy3 + "    " + '%.9f' %z)

j = ncol
for i in range(0,n-abs(j)):
  Ax_j = Ax + 3.0*j*rCC
  Ay_i = Ay + 2.0*i*Ay
  HAx = Ax_j + rCH
  HAy = Ay_i
  Cx_j = Cx + 3.0*j*rCC
  Cy_i = 2.0*i*By
  HCx = Cx_j + rCH
  HCy = Cy_i
  Fx_j1 = Fx - 3.0*j*rCC
  Fy_i1 = -2.0*i*By
  HF1x = Fx_j1 - rCH
  HF1y = Fy_i1
  Dx_j = Dx - 3.0*j*rCC
  Dy_i = -Ay - 2.0*i*Ay
  HDx = Dx_j - rCH
  HDy = Dy_i
  if (n_is_odd == True):
    coordinates.append("H" + "    " + '%.9f' %HCx + "    " + '%.9f' %HCy + "    " + '%.9f' %z)
    if (i != 0):
      coordinates.append("H" + "    " + '%.9f' %HF1x + "    " + '%.9f' %HF1y + "    " + '%.9f' %z)
  else:
    coordinates.append("H" + "    " + '%.9f' %HAx + "    " + '%.9f' %HAy + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HDx + "    " + '%.9f' %HDy + "    " + '%.9f' %z)

j = -ncol
for i in range(0,n-abs(j)):
  Bx_j = Bx + 3.0*j*rCC
  By_i = Ay + 2.0*i*Ay
  HBx = Bx_j - rCH
  HBy = By_i
  Fx_j = Fx + 3.0*j*rCC
  Fy_i = 2.0*i*By
  HFx = Fx_j - rCH
  HFy = Fy_i
  Ex_j = Ex - 3.0*j*rCC
  Ey_i = -Ay - 2.0*i*Ay
  HEx = Ex_j + rCH
  HEy = Ey_i
  Cx_j1 = Cx - 3.0*j*rCC
  Cy_i1 = -2.0*i*By
  HC1x = Cx_j1 + rCH
  HC1y = Cy_i1
  if (n_is_odd == True):
    coordinates.append("H" + "    " + '%.9f' %HFx + "    " + '%.9f' %HFy + "    " + '%.9f' %z)
    if (i != 0):
      coordinates.append("H" + "    " + '%.9f' %HC1x + "    " + '%.9f' %HC1y + "    " + '%.9f' %z)
  else:
    coordinates.append("H" + "    " + '%.9f' %HBx + "    " + '%.9f' %HBy + "    " + '%.9f' %z)
    coordinates.append("H" + "    " + '%.9f' %HEx + "    " + '%.9f' %HEy + "    " + '%.9f' %z)

## write xyz file
natom = nH + nC
outFile = open("graphene-C" + str(nC) + "H" + str(nH) + ".xyz", 'w')
outFile.write(str(natom) + "\n")
outFile.write("Graphene C" + str(nC) + "H" + str(nH) + " in xyz format\n")
for point in coordinates:
  outFile.write(point + "\n")

outFile.close()
