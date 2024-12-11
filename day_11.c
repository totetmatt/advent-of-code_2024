#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void part_1() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_11.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    
    long mem[2][10000000] = {0L};
  
    while ((read = getline(&line, &len, fp)) != -1) {
        
            char *tok = strtok(line," ");
            while(tok != NULL) {
        
                int i = atoi(tok);
                mem[0][i]= 1;
                tok = strtok(NULL," ");
            }
    }
    for(size_t i=1; i<=25;i++) {
        size_t current = 1-i%2;
        size_t next = i%2;
        for(size_t x =0;x<10000000;x++) {
            printf(">%zu\n",x);
            if(mem[current][x]==0) { 

            } else {
                if(x==0) {
                    mem[next][x]+=mem[current][x];
                }
            }
           
        
        }
        break;

    }

    
    
  
    fclose(fp);
    if (line) free(line);
    printf("\n%ld\n",cpt);
}

int main() {

    part_1(); // 1 and 2 
    return 0;
}
