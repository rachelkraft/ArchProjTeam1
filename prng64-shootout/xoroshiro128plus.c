#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include<time.h>
#include "mt64.h"
#include <stdarg.h>
#include <string.h>

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


int main(int argc, char *argv[])
{
    int size;
    
    if (argc == 3){
        size = atoi(argv[1]);
    }
    
    clock_t starting_time, finishing_time;
    FILE * fp;
    /* open the file for writing*/
    fp = fopen (argv[2],"w");
    uint64_t s[]={6287354649,9752954639};
    
    /*Write header*/
    char str[1280];
    char size_str[12];
    sprintf(size_str, "%d", size);
    strcat(str,"#==================================================================\n# generator xoroshiro128plus  seed = 6287354649\n#==================================================================\ntype: d\ncount: ");
    strcat(str,size_str);
    strcat(str,"\nnumbit: 64\n");
    fprintf(fp,"%s",str);
    
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

