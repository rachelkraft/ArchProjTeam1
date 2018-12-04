
TASK 1
So for the first task of 
	Run Shootout.c 30x on your machine
I've written the file run_shootout.sh. This file compiles shootout.c, and then runs it 30 times, and writes the output to a file called "output_shootout_30.txt". If you haven't already, run this script by running the commands:

./run_shootout.sh

And then send me your resulting file: "output_shootout_30.txt" and I will compile the results into a graph

TASK 2
For the second task of:
	2. Generate 1,5, and 10 million random numbers with all 4 algorithms on your machine and record the time it takes (if you can do 10x each)

For that there is a file run_4algs_generate_random_numbers.sh. This file compiles the algorithm .c files,  runs 10 iterations of generating 1,5, and 10 million numbers with all 4 algorithms, times them, and outputs the times. The result files are output into a new directory that is created called "results". There will be 6 output files for each algorithm (so 24 files total). This is because there are 3 files, each with 10 timings for generating 1,5, and 10 million respectively. (The naming convention for these files is: results/algorithm_name-timings-number_of_generated_random_numbers-rand-nums.txt) Then there are 3 more files containing the actual random numbers generated. (The naming convention for these files is: results/algorithm_name-generate-number_of_generated_random_numbers-rand-nums.txt).

If you haven't already gotten these values, run the commands:

./run_4algs_generate_random_numbers.sh

And then send ALL me the resulting files, and I can compile them into graphs. 

TASK 3
Finally for the third task of:

	3. Generate 60 million numbers with your specific algorithm

This will take a few commands. First a file of 60 million numbers needs to be generated. This can be done by the following commands

#compile individual algorithm code
gcc algorithm_name.c -o algorithm_name
#run compiled code with input of number of randnums to generate and output filename
./algorithm_name  number_of_rand_nums_to_generate  file_name_rand_nums.txt
#feed random number file into dieharder
dieharder -g 202 -f file_name_rand_nums.txt -a > dieharder_outputfile.txt

For example if I wanted to do this for my spcg64 algorithm, for 60million numbers, I would run the following commands:

gcc spcg64.c -o spcg64

./spcg64 60000000 "results/spcg64-generate-60000000-rand-nums.txt"

dieharder -g 202 -f "results/spcg64-generate-60000000-rand-nums.txt" -a > "spcg64-dieharder-output-60000000-nums.txt"


(The above assumes that you are storing your results in a folder called "results")



Once you do this, send the dieharder_outputfile.txt and we can compile statistics like: number of FAILED tests, number of WEAK tests, number of PASSED tests.



INDIVIDUALLY RUNNING ALGORITHMS

If you want to run the algorithms individually to generate an amount of random numbers, you can use the following commands:

gcc   algorithm_name.c   algorithm_name
./algorithm_name   number_of_rand_nums   output_file_name.txt