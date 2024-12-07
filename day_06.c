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
    const char * filename ="day_06.txt";

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
    int cpt =1;
    while(1) {
        struct vec2 next = {guard.x+direction.x,guard.y+direction.y};
        if(next.x<0 || next.x>=width || next.y <0 || next.y>=height) {
    
            break;
        }
        if(map[next.y][next.x]=='#') {
            if(direction.y==-1) {
                direction.x = 1;
                direction.y = 0;
            } else if(direction.x == 1) {
                direction.x = 0;
                direction.y = 1;
            } else if (direction.y == 1) {
                direction.x = -1;
                direction.y = 0;
            } else if (direction.x == -1) {
                direction.x=0;
                direction.y = -1.;
            }
            continue;
        }
        guard = next;
        if(visited[guard.y][guard.x]==0) {
            visited[guard.y][guard.x]=1;
            cpt++;
        }
    }



    fclose(fp);
    if (line) free(line);
    printf("%i\n",cpt);
}
void part_2(){    
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_06.txt";

    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

  

    char map[130][130] = {0};
    int width = 0;
    int height = 0;

    struct vec2 guard = {0};
    struct vec2 direction = {0,-1};
struct vec2 orig_direction = {0,-1};
    struct vec2 orig_guard = {0};

    struct vec2 visited[8096];
    struct vec2* p_visited=visited;
    while ((read = getline(&line, &len, fp)) != -1) {

        int line_len =width=strlen(line)-1;

        memcpy(map[height],line,line_len);
        for(int i=0;i<width;i++) {
            if(map[height][i]=='^') {
                map[height][i] = '.';
                guard.y = height;
                guard.x = i;
                orig_guard.y = height;
                orig_guard.x = i;
            }

        }
        
  
        height++;
    }

   
    int cpt =0;
    *p_visited=guard;
    p_visited++;
    while(1) {
        struct vec2 next = {guard.x+direction.x,guard.y+direction.y};
        if(next.x<0 || next.x>=width || next.y <0 || next.y>=height) {
    
            break;
        }
        if(map[next.y][next.x]=='#') {
            
            if(direction.y==-1) {
                direction.x = 1;
                direction.y = 0;
            } else if(direction.x == 1) {
                direction.x = 0;
                direction.y = 1;
            } else if (direction.y == 1) {
                direction.x = -1;
                direction.y = 0;
            } else if (direction.x == -1) {
                direction.x=0;
                direction.y = -1.;
            }
            continue;
        }
        guard = next;
        *p_visited=guard;
        p_visited++;
    }

    int solution[130][130]={0};
    for(size_t check=0;check < (p_visited-visited);check++) {

        int block[130][130][4] = {0};
        struct vec2 add_block = visited[check];

         if(add_block.x==orig_guard.x && add_block.y == orig_guard.y) continue;;
         guard = orig_guard;
         direction = orig_direction;


        while(1) {
            struct vec2 next = {guard.x+direction.x,guard.y+direction.y};
            if(next.x<0 || next.x>=width || next.y <0 || next.y>=height) {
                
                break;
            }
        if(map[next.y][next.x]=='#' || next.x==add_block.x && next.y==add_block.y) {
            if(block[next.y][next.x][(direction.y==0? (direction.x==-1?0:1) : (direction.y==-1?2:3))]==1) {
                if(solution[add_block.y][add_block.x] ==0){
                    solution[add_block.y][add_block.x]=1;
                    cpt +=1;
                }
                break;
                
            } 
            block[next.y][next.x][(direction.y==0? (direction.x==-1?0:1) : (direction.y==-1?2:3))]=1;
            
            if(direction.y==-1) {
                direction.x = 1;
                direction.y = 0;
            } else if(direction.x == 1) {
                direction.x = 0;
                direction.y = 1;
            } else if (direction.y == 1) {
                direction.x = -1;
                direction.y = 0;
            } else if (direction.x == -1) {
                direction.x=0;
                direction.y = -1.;
            }
            continue;
        }
            guard = next;
        }
    }

    fclose(fp);
    if (line) free(line);
    printf("%i\n",cpt);
}
int main() {

    part_1();
    part_2();
    return 0;
}
