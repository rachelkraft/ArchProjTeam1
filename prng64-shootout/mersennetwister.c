#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include<time.h>
#include "mt64.h"
#include <stdarg.h>
#include <string.h>


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
    struct mt64 mt64[1];
    mt_init(mt64, UINT64_C(0xdeadbeefcafebabe));
    
    /*Write header*/
    char str[1280];
    char size_str[12];
    sprintf(size_str, "%d", size);
    strcat(str,"#==================================================================\n# generator mersennetwister  seed = 0xdeadbeefcafebabe\n#==================================================================\ntype: d\ncount: ");
    strcat(str,size_str);
    strcat(str,"\nnumbit: 64\n");
    fprintf(fp,"%s",str);
    
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


