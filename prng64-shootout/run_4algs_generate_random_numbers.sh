#!/bin/bash

# make a directory to store results
mkdir results
declare -a arr=(1000000 5000000 10000000)

#clear the timing results files before we append
for i in "${arr[@]}"
do
    echo -n "" > "results/spcg64-timings-$i-rand-nums.txt"
    echo -n "" > "results/xoroshiro128plus-timings-$i-rand-nums.txt"
    echo -n "" > "results/xorshift128plus-timings-$i-rand-nums.txt"
    echo -n "" > "results/mersennetwister64-timings-$i-rand-nums.txt"
done

gcc spcg64.c -o spcg64
gcc xoroshiro128plus.c -o xoroshiro128plus
gcc xorshift.c -o xorshift128plus
gcc mersennetwister.c -o mersennetwister64

for i in "${arr[@]}"
do
    for run in {1..10}
    do
        ./spcg64 $i "results/spcg64-generate-$i-rand-nums.txt" >> "results/spcg64-timings-$i-rand-nums.txt"
        ./xoroshiro128plus $i "results/xoroshiro128plus-generate-$i-rand-nums.txt" >> "results/xoroshiro128plus-timings-$i-rand-nums.txt"
        ./xorshift128plus $i "results/xorshift-generate-$i-rand-nums.txt" >> "results/xorshift128plus-timings-$i-rand-nums.txt"
        ./mersennetwister64 $i "results/mersennetwister64-generate-$i-rand-nums.txt" >> "results/mersennetwister64-timings-$i-rand-nums.txt"
    done
done

