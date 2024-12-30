#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int solve(int *map[][71],int width,int height){

    for(int y=0;y<height;y++){
        for(int x=0;x<width;x++) {
            if(map[y][x]==0)
            printf(".");
            else
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
void part_1() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_18.test.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);


    int time = 1;
    int width = 7;
    int height = 7;
    int map[71][71] = {0};
    memset(map,0,sizeof(int)*71*71);
    solve(map,width,height);
    while ((read = getline(&line, &len, fp)) != -1) {
            int x=atoi(strtok(line,","));
            int y=atoi(strtok(NULL,","));
            map[y][x]= time;
            time++;
    }
    
   

    fclose(fp);
    if (line) free(line);
    printf("\n%ld\n",cpt);
}

int main() {

    part_1(); // 1 and 2 

    return 0;
}
