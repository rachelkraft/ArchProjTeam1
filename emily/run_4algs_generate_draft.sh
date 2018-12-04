#!/bin/bash

##### EDIT THE VARIABLES BELOW FOR YOUR SPECIFIC NEEDS #####

# your results directory
dir_path=/home/emily/Projects/ArchProjTeam1/emily

num_repeats=10

count_nums[0]=1000000
count_nums[1]=5000000
count_nums[2]=10000000
count_nums[3]=60000000
count_nums[4]=100000000


label_nums[0]='1mil'
label_nums[1]='5mil'
label_nums[2]='10mil'
label_nums[3]='60mil'
label_nums[4]='100mil'

##################################################

#clear the timing results files before we append
for ((i=0; i<${#count_nums[*]}; i++))
do
    #echo $i
    #echo ${count_nums[i]}
    #echo ${label_nums[i]}
    echo -n "" > "${dir_path}/spcg64-generate-${label_nums[i]}-rand-nums.txt" 
    echo -n "" > "${dir_path}/xoroshiro128plus-generate-${label_nums[i]}-rand-nums.txt"
    echo -n "" > "${dir_path}/xorshift-generate-${label_nums[i]}-rand-nums.txt"
    echo -n "" > "${dir_path}/mersennetwister64-generate-${label_nums[i]}-rand-nums.txt"
done

gcc spcg64.c -o spcg64
gcc xoroshiro128plus.c -o xoroshiro128plus
gcc xorshift.c -o xorshift128plus
gcc mersennetwister.c -o mersennetwister64

date '+%R %a %d %b %Y'

for ((i=0; i<${#count_nums[*]}; i++))
do
    for run in $(seq $num_repeats)
    do
        #echo $run
        ./spcg64 $i "${dir_path}/mersennetwister64-generate-${label_nums[i]}-rand-nums.txt" >> "${dir_path}/spcg64-timings-${label_nums[i]}-rand-nums.txt"
        ./xoroshiro128plus $i "${dir_path}/xoroshiro128plus-generate-${label_nums[i]}-rand-nums.txt" >> "${dir_path}/xoroshiro128plus-timings-${label_nums[i]}-rand-nums.txt"
        ./xorshift128plus $i "${dir_path}/xorshift-generate-${label_nums[i]}-rand-nums.txt" >> "${dir_path}/xorshift128plus-timings-${label_nums[i]}-rand-nums.txt"
        ./mersennetwister64 $i "${dir_path}/mersennetwister64-generate-${label_nums[i]}-rand-nums.txt" >> "${dir_path}/mersennetwister64-timings-${label_nums[i]}-rand-nums.txt"
    done
    echo "  Finished generation for ${label_nums[i]}."
done

date '+%R %a %d %b %Y'
