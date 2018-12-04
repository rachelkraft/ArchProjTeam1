#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include<time.h>
#include "mt64.h"
#include <stdarg.h>
#include <string.h>

uint64_t spcg64(uint64_t s[2])
{
    uint64_t m  = 0x9b60933458e17d7d;
    uint64_t a0 = 0xd737232eeccdf7ed;
    uint64_t a1 = 0x8b260b70b8e98891;
    uint64_t p0 = s[0];
    uint64_t p1 = s[1];
    s[0] = p0 * m + a0;
    s[1] = p1 * m + a1;
    int r0 = 29 - (p0 >> 61);
    int r1 = 29 - (p1 >> 61);
    uint64_t high = p0 >> r0;
    uint32_t low  = p1 >> r1;
    return (high << 32) | low;
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
    strcat(str,"#==================================================================\n# generator spcg64  seed = 6287354649\n#==================================================================\ntype: d\ncount: ");
    strcat(str,size_str);
    strcat(str,"\nnumbit: 64\n");
    fprintf(fp,"%s",str);
    
    int i;
    starting_time = clock();
    /* write lines of text into the file stream*/
    for(i = 0; i < size;i++){
        fprintf (fp, "%" PRIu64 "\n",spcg64(s));
    }
    finishing_time = clock();
    /* close the file*/
    fclose (fp);
    printf("\nTotal Time For Execution:\t%ld\n", finishing_time - starting_time);
    //printf("spcg64:\n");
    //printf("%" PRIu64 "\n", spcg64(s));
    
    
    return 0;
}
