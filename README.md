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


## Convert BAGEL input into xyz input
More information on BAGEL can be found [here](https://nubakery.org).

### BAGEL to xyz

`bagel2xyz.py` converts BAGEL input file `filename.json` into xyz format `filename.xyz`.

BAGEL input file example is in `hf.json`. This is a very simple calculation for
HF molecule using STO-3G basis set and TZVPP-jkfit fitting basis. Note that
the coordinates should be in Angstrom.

```
{ "bagel" : [

{
  "title" : "molecule",
  "symmetry" : "C1",
  "basis" : "sto-3g",
  "df_basis" : "tzvpp-jkfit",
  "angstrom" : "true",
  "geometry" : [
    { "atom" : "H", "xyz" : [     -0.000000000,   -0.000000000,    0.305956000] },
    { "atom" : "F", "xyz" : [     -0.000000000,   -0.000000000,    2.720616000] }
  ]
},

{
  "title" : "hf",
  "thresh" : 1.0e-10
}

]}
```

Output `hf.xyz` file:
```
2
hf.json in xyz format
H    -0.000000000    -0.000000000    0.305956000
F    -0.000000000    -0.000000000    2.720616000
```

### xyz to BAGEL

Now, you can do the reverse, that is, converting xyz file into BAGEL input file
using `xyz2bagel.sh`. You will be asked to provide the name of the xyz file, basis set,
as well as fitting basis set, and the method you want to use.

```
Usage:
./xyz2bagel xyzfile basis df_basis method
```

For example, to recreate `hf.json` from `hf.xyz`, you can do:

```
./xyz2bagel.sh hf.xyz sto-3g tzvpp-jkfit hf > hf.json
```

### BAGEL to Turbomole inputs

`bagel2turbomole.py` converts BAGEL input file into a coordinate file `coord` used
by the package [Turbomole](http://www.turbomole-gmbh.com).

This is an example for `coord` generated using `hf.json`.

```
$coord
-0.000000000    -0.000000000    0.305956000       h
-0.000000000    -0.000000000    2.720616000       f
$user-defined bonds
$end
```

Well, if you are using Turbomole, you may need to specify the basis and fitting basis,
especially if the basis sets you are using are not in the library (or you aren't sure).
It's always good to know exactly what basis set you are using.

`bagel2turbomole-basis.sh` converts basis set in json format to a format used by Turbomole.
You will need to specify if you want it to be basis or fitting basis. An example is given for
Gd in `gd-dz.json` to generate a `basis` file,

```
./bagel2turbomole-basis.sh gd-dz.json basis > basis
```

and also `gd-dz-jkfit.json` to generate  an `auxbasis` file.

```
./bagel2turbomole-basis.sh gd-dz-jkfit.json jkbas > auxbasis
```

This files `basis` and `auxbasis` follow Turbomole's naming convention, ready to be used.
