#include <stdio.h>
#include <stdlib.h>
#include <string.h>



struct vec2 {
    int x;
    int y;
};
void part_1() {
FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_06.test.txt";

    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

  

    char map[130][130] = {0};
    int visited[130][130] = {0};
    int width = 0;
    int height = 0;

    struct vec2 guard = {0};
    struct vec2 direction = {0,-1};
    while ((read = getline(&line, &len, fp)) != -1) {

        int line_len =width=strlen(line)-1;

        memcpy(map[height],line,line_len);
        for(int i=0;i<width;i++) {
            if(map[height][i]=='^') {
                map[height][i] = '.';
                guard.y = height;
                guard.x = i;
            }

        }
        
  
        height++;
    }

    visited[guard.y][guard.x]=1;
    int cpt =0;
    while(1) {
        struct vec2 next = {guard.x+direction.x,guard.y+direction.y};
        if(next.x<0 || next.x>=width || next.y <0 || next.y>=height) {
            printf("Outside map");
            break;
        }
        if(map[next.y][next.x]=='#') {
            if(next.y==-1) {
                next.x = 1;
                next.y = 0;
            } else if(next.x == 1) {
                next.x = 0;
                next.y = 1;
            } else if (next.y == 1) {
                next.x = -1;
                next.y = 0;
            } else if (next.x == -1) {
                next.x=0;
                next.y = 1.;
            }
        }
        break;
    }



    fclose(fp);
    if (line) free(line);
    printf("%i\n",cpt);
}
void part_2(){    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_06.test.txt";

    int cpt = 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

  


    while ((read = getline(&line, &len, fp)) != -1) {

    

    }


    fclose(fp);
    if (line) free(line);
    printf("%i\n",cpt);
}
int main() {

    part_1();
    //part_2();
    return 0;
}
