# Scripts

Python scripts have been tested on Python 3.

## Generate coordinates for hydrocarbons 
`gen_alkanes.py` generates xyz coordinates for alkanes of the form H-(C2H4)n-H
given n. An example for n=3 is given in the output file `C6H14.xyz`. An image of this molecule
viewed with Avogadro is given in `C6H14.png`.

`gen_C2H2_n.py` generates xyz coordinates for polyacetylenes of the form (C2H2)n
given n. An example for n=3 is given in the output file `C6H8.xyz`. An image of this molecule
viewed with Avogadro is given in `C6H8.png`.

## Generate coordinates for graphene sheets
`gen_graphene_sheets_circH.py` generates xyz coordinates for 'circular' hydrogenated graphene sheets of the form
`C_{6n^2}H_{6n}` given n. For n=1, we just get a single benzene molecule (see file `graphene-C6H6.xyz`
and `graphene-C6H6.png`). Two examples are given for n=2 and n=5 with images of the sheets viewed
with Avogadro in `graphene-C24H12.xyz` and `graphene-C24H12.png` (n=2) and `graphene-C150H30.xyz`
and `graphene-C150H30.png`.

`gen_graphene_sheets.py` generates xyz coordinates for rectangular graphene sheets (without hydrogen atoms)
given n to be the number of carbon atoms. An example for n=5 is given in `graphene-C190.xyz`. Again, a
visualization for the sheet via Avogadro is given in `graphene-C190.png`. Users will need to manually add
hydrogen atoms or modify the script to do so before running any calculations!

## Generate coordinates of randomly distributed points in box
`gen_points.py` generates xyz coordinates for n points randomly distributed in a box of length a in Angstrom.
This might be useful in simulation, for example, when the given coordinates are of the centers of mass
of molecules such as water molecules. Just for visualization, the points are labeled as Helium atoms
in the generated `cube.xyz` and `cube.json` file, the latter is used in BAGEL (refer to nubakery.org for more details
on this package). An example is given for n=70 and a=50.1 here.
