#!/bin/bash
echo -n "" > output_shootout_25.txt
for run in {1..25}
do
  ./shootout >> output_shootout_25.txt
  echo "/////////////////////\n" >> output_shootout_25.txt
done
