#include <stdint.h>
#include <stdio.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include<time.h>
#include "mt64.h"

uint64_t xoroshiro128plus(uint64_t s[2])
{
    uint64_t s0 = s[0];
    uint64_t s1 = s[1];
    uint64_t result = s0 + s1;
    s1 ^= s0;
    s[0] = ((s0 << 24) | (s0 >> 40)) ^ s1 ^ (s1 << 16);
    s[1] = (s1 << 37) | (s1 >> 27);
    return result;
}


int main()
{
    int size=1000000;
    clock_t starting_time, finishing_time;
    FILE * fp;
    /* open the file for writing*/
    fp = fopen ("Xoroshiro128plus_60mill.txt","w");
    uint64_t s[]={6287354649,9752954639};
    /*Write header*/
    fprintf (fp, "#==================================================================\n# generator xoroshiro128plus  seed = 6287354649\n#==================================================================\ntype: d\ncount: 60000000\nnumbit: 64\n");
    int i;
    starting_time = clock();
    /* write lines of text into the file stream*/
    for(i = 0; i < size;i++){
        fprintf (fp, "%" PRIu64 "\n",xoroshiro128plus(s));
    }
    finishing_time = clock();
    /* close the file*/
    fclose (fp);
    printf("\nTotal Time For Execution:\t%ld\n", finishing_time - starting_time);
    //printf("xoroshiro128plus:\n");
    //printf("%" PRIu64 "\n", xoroshiro128plus(s));
    
    
    return 0;
}

