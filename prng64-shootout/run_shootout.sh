#!/bin/bash

#clear the output file before we append to it
echo -n "" > output_shootout_30.txt

#compile shootout.c
make

for run in {1..30}
do
  ./shootout >> output_shootout_30.txt
  echo "/////////////////////\n" >> output_shootout_30.txt
done
