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
    const char * filename ="day_10.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    int MAP[54][54]={-1};

    struct vec2 start[4096]= {0};
    struct vec2  *p_start =start;
    size_t width=0;
    size_t height=0;
    while ((read = getline(&line, &len, fp)) != -1) {
            width = strlen(line);
            if(line[0]=='\n') break;
            for(size_t x=0;x<width;x++){
                if(line[x]=='.'){
                    MAP[height][x]=-1;
                    continue;
                }
                if(line[x]=='\n') continue;
                MAP[height][x] = line[x] -48;
                if(MAP[height][x]==0) {
                    p_start->x=x;
                    p_start->y=height;
                    p_start++;
                }
            }
            height ++;

    }
    size_t s_start =(p_start-start);

    for(size_t i=0;i<s_start;i++) {
        int summit[54][54]={0};
        struct vec2 next[20000] = {0};
        next[0] = start[i];
        struct vec2 *p_next_e =next+1;  
        struct vec2 *p_next_s =next; 
        //printf(">>>>(%i,%i)\n",start[i].y,start[i].x);
        while(p_next_s<p_next_e) {
            //printf("(%i,%i)\n",p_next_s->y,p_next_s->x);
            for(int dy=-1;dy<=1;dy+=2){
                if(p_next_s->y+dy <0 || p_next_s->y+dy>= height ) continue;
                if( MAP[p_next_s->y+dy][p_next_s->x] == MAP[p_next_s->y][p_next_s->x]+1 ){
                    if(MAP[p_next_s->y+dy][p_next_s->x]==9) {
                        if(summit[p_next_s->y+dy][p_next_s->x]!=1){
                            summit[p_next_s->y+dy][p_next_s->x] =1;
                            cpt++;
                        }
                        continue;
                    }
                    p_next_e->x = p_next_s->x;
                    p_next_e->y = p_next_s->y+dy;
                    p_next_e++;
                };
            }
            for(int dx=-1;dx<=1;dx+=2){
                if(p_next_s->x+dx <0 || p_next_s->x+dx>= width )  continue;
                if(MAP[p_next_s->y][p_next_s->x+dx] == MAP[p_next_s->y][p_next_s->x]+1 ){
                    if(MAP[p_next_s->y][p_next_s->x+dx]==9) {
                        if(summit[p_next_s->y][p_next_s->x+dx]!=1){
                            summit[p_next_s->y][p_next_s->x+dx] =1;
                            cpt++;
                        }
                        continue;
                    }
                    p_next_e->x = p_next_s->x+dx;
                    p_next_e->y = p_next_s->y;
                    p_next_e++;
                };
            }
            p_next_s++;
        } 


    }
    
  
    fclose(fp);
    if (line) free(line);
    printf("%ld\n",cpt);
}
void part_2() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_10.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    int MAP[54][54]={-1};

    struct vec2 start[4096]= {0};
    struct vec2  *p_start =start;
    size_t width=0;
    size_t height=0;
    while ((read = getline(&line, &len, fp)) != -1) {
            width = strlen(line);
            if(line[0]=='\n') break;
            for(size_t x=0;x<width;x++){
                if(line[x]=='.'){
                    MAP[height][x]=-1;
                    continue;
                }
                if(line[x]=='\n') continue;
                MAP[height][x] = line[x] -48;
                if(MAP[height][x]==0) {
                    p_start->x=x;
                    p_start->y=height;
                    p_start++;
                }
            }
            height ++;

    }
    size_t s_start =(p_start-start);

    for(size_t i=0;i<s_start;i++) {
        int summit[54][54]={0};
        struct vec2 next[20000] = {0};
        next[0] = start[i];
        struct vec2 *p_next_e =next+1;  
        struct vec2 *p_next_s =next; 
        //printf(">>>>(%i,%i)\n",start[i].y,start[i].x);
        while(p_next_s<p_next_e) {
            //printf("(%i,%i)\n",p_next_s->y,p_next_s->x);
            for(int dy=-1;dy<=1;dy+=2){
                if(p_next_s->y+dy <0 || p_next_s->y+dy>= height ) continue;
                if( MAP[p_next_s->y+dy][p_next_s->x] == MAP[p_next_s->y][p_next_s->x]+1 ){
                    if(MAP[p_next_s->y+dy][p_next_s->x]==9) {
                   
                            cpt++;
                       
                        continue;
                    }
                    p_next_e->x = p_next_s->x;
                    p_next_e->y = p_next_s->y+dy;
                    p_next_e++;
                };
            }
            for(int dx=-1;dx<=1;dx+=2){
                if(p_next_s->x+dx <0 || p_next_s->x+dx>= width )  continue;
                if(MAP[p_next_s->y][p_next_s->x+dx] == MAP[p_next_s->y][p_next_s->x]+1 ){
                    if(MAP[p_next_s->y][p_next_s->x+dx]==9) {
                    
                            cpt++;
                      
                        continue;
                    }
                    p_next_e->x = p_next_s->x+dx;
                    p_next_e->y = p_next_s->y;
                    p_next_e++;
                };
            }
            p_next_s++;
        } 


    }
    
  
    fclose(fp);
    if (line) free(line);
    printf("%ld\n",cpt);
}
int main() {

    part_1();
     part_2();
    return 0;
}
