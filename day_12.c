#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void part_1() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_12.test.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    char map[140][140];
    char mask[140][140];


    int width  = 0;
    int height = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        width = strlen(line)-1;
        memcpy(map[height],line,sizeof(char)*width);
        height++;
    }
    for(size_t y=0;y<height;y++) {
        for(size_t x=0;x<width;x++) {
            printf("%c",map[y][x]);
        }
        printf("\n");
    }
    fclose(fp);
    if (line) free(line);
    printf("\n%ld\n",cpt);
}

int main() {

    part_1(); // 1 and 2 

    return 0;
}
