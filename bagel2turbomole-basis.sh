#!/bin/bash
##### 
##### Author: Hai-Anh Le
#####

if [[ "$#" -ne 2 ]]; then
  echo 'Usage: ./bagel2turbomole.sh filename.json basis/jkbas'
  exit
fi

fl=$1
basis=$2
stem=`echo $fl | cut -d '.' -f 1`

echo '$'$basis
echo '*'
element=`awk '/\"\ \:\ \[/ {print $1}' $fl | awk 'NR==1,NR==1 {print $1}' | sed s/\"//g | tr '[:upper:]' '[:lower:]'`
echo $element' '$stem
echo '*'
nb=`awk '/angular/ {print NR}' $fl | wc -l`
set `awk '/angular/ {print NR}' $fl`
for ln
do
  ang=`awk 'NR=='$ln',NR=='$ln' {print $3}' $fl | sed s/\"//g | cut -d ',' -f 1`
  awk 'NR=='$ln'+1,NR=='$ln'+1' $fl | sed 's/\"prim\"\ \:\ \[//g' | sed 's/\]\,//g' | sed 's/\,/\n/g'| sed 's/\ //g' > prim
  awk 'NR=='$ln'+2,NR=='$ln'+2' $fl | sed 's/\"cont\"\ \:\ \[\[//g' | sed 's/\]\]//g' | sed 's/\,/\n/g' | sed 's/\ //g' > cont
  nprim=`wc -l prim | awk '{print $1}'`
  echo $nprim' '  ' '$ang
# paste prim cont | sed -e 's/^[ \t]*/    /'
  i=1
  while [[ "$i" -le "$nprim" ]]; do
    p=`awk 'NR=='$i',NR=='$i' {print $1}' prim`
    c=`awk 'NR=='$i',NR=='$i' {print $1}' cont`
    echo $p'     '$c
    let i=$i+1
  done
done
echo '*'
echo '$end'
rm -f prim cont
