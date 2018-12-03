#!/bin/bash
echo -n "" > output_rand_nums_spcg.txt
echo -n "" > output_rand_nums_xoroshiro128plus.txt
echo -n "" > output_rand_nums_xorshift128plus.txt

gcc spcg64.c -o spcg
gcc xoroshiro128plus.c -o xoroshiro128plus
gcc xorshift.c -o xorshift128plus

for run in {1..10}
do
./spcg >> output_rand_nums_spcg.txt
./xoroshiro128plus >> output_rand_nums_xoroshiro128plus.txt
./xorshift128plus >> output_rand_nums_xorshift128plus.txt
done
