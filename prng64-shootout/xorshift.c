#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include<time.h>
#include "mt64.h"
#include <stdarg.h>
#include <string.h>

uint64_t xorshift128pluss(uint64_t s[2])
{
    uint64_t x = s[0];
    uint64_t y = s[1];
    s[0] = y;
    x ^= x << 23;
    s[1] = x ^ y ^ (x >> 17) ^ (y >> 26);
    return s[1] + y;
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
    uint64_t s[]={3632348380,9752954639};
    
    /*Write header*/
    char str[1280];
    char size_str[12];
    sprintf(size_str, "%d", size);
    strcat(str,"#==================================================================\n# generator xoroshift128plus  seed = 6287354649\n#==================================================================\ntype: d\ncount: ");
    strcat(str,size_str);
    strcat(str,"\nnumbit: 64\n");
    fprintf(fp,"%s",str);
    
    int i;
    starting_time = clock();
    /* write 60000000 lines of text into the file stream*/
    for(i = 0; i < size;i++){
       fprintf (fp, "%" PRIu64 "\n",xorshift128pluss(s));
    }
    finishing_time = clock();
   /* close the file*/  
   fclose (fp);
   printf("\nTotal Time For Execution:\t%ld\n", finishing_time - starting_time);
    //printf("xorshift:\n");
   // printf("%" PRIu64 "\n", xorshift128pluss(s));
    //printf("%" PRIu64 "\n", xorshift128pluss(s));
    //printf("%" PRIu64 "\n", xorshift128pluss(s));
   
    return 0;
}


