#!/bin/bash

### This script converts xyz coordinates into bagel input format with London orbitals

if [ $# -ne 4 ]
  then
     echo Usage: 
     echo './xyz2bagel xyzfile basis df_basis method'
     echo
     exit
fi

fl=$1
basis=$2
df=$3
method=$4

echo '{ "bagel" : ['
echo
echo '{'
echo '  "title" : "molecule",'
echo '  "symmetry" : "C1",'
echo '  "basis" : "'$basis'",'
echo '  "df_basis" : "'$df'",'
echo '  "angstrom" : "true",'
echo '  "geometry" : ['
nat=`awk 'NR==1,NR==1 {print $1}' $fl`
i=1
while [[ "$i" -le "$nat" ]]; do
  symb=`awk 'NR=='$i'+2,NR=='$i'+2 {print $1}' $fl`
  x=`awk 'NR=='$i'+2,NR=='$i'+2 {print $2}' $fl`
  y=`awk 'NR=='$i'+2,NR=='$i'+2 {print $3}' $fl`
  z=`awk 'NR=='$i'+2,NR=='$i'+2 {print $4}' $fl`
  printf '    { "atom" : "'$symb'", "xyz" : [  '
  printf "%15.9f" $x
  printf ','
  printf "%15.9f" $y
  printf ','
  printf "%15.9f" $z
  if [[ "$i" -lt "$nat" ]]; then
    printf '] },'"\n"
  else
    printf '] }'"\n"
  fi
  let i=$i+1
done
echo '  ]'
echo '},'
echo
echo '{'
echo '  "title" : "'$method'",'
echo '  "thresh" : 1.0e-10'
echo '}'
echo
echo ']}'
