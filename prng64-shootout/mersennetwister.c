#include <stdint.h>
#include <stdio.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include<time.h>
#include "mt64.h"



int main()
{
    int size=60000000;
    clock_t starting_time, finishing_time;
    FILE * fp;
    /* open the file for writing*/
    fp = fopen ("MersenneTwister_60mill.txt","w");
    struct mt64 mt64[1];
    mt_init(mt64, UINT64_C(0xdeadbeefcafebabe));
    /*Write header*/
    fprintf (fp, "#==================================================================\n# generator mersennetwister  seed = 0xdeadbeefcafebabe\n#==================================================================\ntype: d\ncount: 60000000\nnumbit: 64\n");
    int i;
    starting_time = clock();
    /* write lines of text into the file stream*/
    for(i = 0; i < size;i++){
        fprintf (fp, "%" PRIu64 "\n",mt_rand(mt64));
    }
    finishing_time = clock();
    /* close the file*/
    fclose (fp);
    printf("\nTotal Time For Execution:\t%ld\n", finishing_time - starting_time);
    //printf("mersennetwister:\n");
    //printf("%" PRIu64 "\n", mt_rand(mt64));
    
    
    return 0;
}


