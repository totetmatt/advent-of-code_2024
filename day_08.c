#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct vec2 {
    int x;
    int y;
} vec2 ;
void add(struct vec2 *a,struct vec2 *b,struct vec2 *r) {
   r->x = a->x + b->x;
   r->y = a->y +b->y;
}
void sub(struct vec2 *a,struct vec2 *b,struct vec2 *r) {
   r->x = a->x - b->x;
   r->y = a->y - b->y;
}
void mul(struct vec2 *a,int scalar,struct vec2 *r) {
    r->x = a->x * scalar;
    r->y = a->y * scalar;
}

struct Antenna  {
    char id;
    struct vec2 pos;
} Antenna;
void part_1() {
FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_08.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    char map[50][50] = {0} ;
    int antinode[50][50] = {0} ;
    int height= 0;
    int width = 0;
    struct Antenna a[512] = {0};
    struct Antenna *p_a= a;
    while ((read = getline(&line, &len, fp)) != -1) {
            if(line[0]=='\n') break;
            width = strlen(line)-1;
            memcpy(map[height],line,width);
            for(size_t x =0;x<width;x++) {
                if(line[x]!='.') {
                    p_a->id = line[x];
                    p_a->pos.x = x;
                    p_a->pos.y = height;
                    p_a++;
                }
            }
            height ++;
     }
    
    for(struct Antenna *p_l = a;p_l!=p_a;p_l++) {
        for(struct Antenna *p_r = p_l+1;p_r!=p_a;p_r++) {
            if(p_l->id==p_r->id) {
                
                struct Antenna *a=p_l;
                struct Antenna *b=p_r;
                for(int z=0;z<=1;z++) {
                //printf("%c:(%i,%i)--(%i,%i)\n",a->id,a->pos.x,a->pos.y,b->pos.x,b->pos.y);
                    struct vec2 unit_v,unit_v2,a_v1,a_v2,b_v1,b_v2;
                    
                    sub(&a->pos,&b->pos,&unit_v);
                    
                    
                    mul(&unit_v,2,&unit_v2);
                  
                    add(&a->pos,&unit_v,&a_v1);
                    add(&a->pos,&unit_v2,&a_v2);
                    add(&b->pos,&unit_v,&b_v1);
                    add(&b->pos,&unit_v2,&b_v2);   
                    //printf("(%i,%i)=(%i,%i)\n",a_v1.x,a_v1.y,b_v2.x,b_v2.y);
                    if(a_v1.x == b_v2.x && a_v1.y==b_v2.y) {

                   
                        if(a_v1.x >=0  && a_v1.x < width 
                        && a_v1.y >=0 && a_v1.y < height
                        && antinode[a_v1.y][a_v1.x]!= 1) {
                            antinode[a_v1.y][a_v1.x] = 1;
                            cpt ++;
                        }
                    }
                    if(a_v2.x == b_v1.x && a_v2.y==b_v1.y) {
    
                        if(a_v2.x >=0  && a_v2.x < width && a_v2.y >=0 && a_v2.y < height
                        && antinode[a_v2.y][a_v2.x]!= 1) {
                            antinode[a_v2.y][a_v2.x] = 1;
                            cpt ++;
                        }
                    }
                    a=p_r;
                    b=p_l;
                }

            }
        }
    }
    /*
    for(size_t y = 0;y < height;y++){
        for(size_t x= 0;x<width;x++){
            printf("%c",map[y][x]);
        }
        printf("\n");
    }*/

    
    fclose(fp);
    if (line) free(line);
    printf("%lld\n",cpt);
}
void part_2(){  
FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_08.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    char map[50][50] = {0} ;
    int antinode[50][50] = {0} ;
    int height= 0;
    int width = 0;
    struct Antenna a[512] = {0};
    struct Antenna *p_a= a;
    while ((read = getline(&line, &len, fp)) != -1) {
            if(line[0]=='\n') break;
            width = strlen(line)-1;
            memcpy(map[height],line,width);
            for(size_t x =0;x<width;x++) {
                if(line[x]!='.') {
                    p_a->id = line[x];
                    p_a->pos.x = x;
                    p_a->pos.y = height;
                    p_a++;
                }
            }
            height ++;
     }
    
    for(struct Antenna *p_l = a;p_l!=p_a;p_l++) {
        for(struct Antenna *p_r = p_l+1;p_r!=p_a;p_r++) {
            if(p_l->id==p_r->id) {
                
                struct Antenna *a=p_l;
                struct Antenna *b=p_r;
                for(int z=0;z<=1;z++) {
         
                    struct vec2 unit_v,unit_vs,a_v;
                    
                    sub(&a->pos,&b->pos,&unit_v);
                    
                    int scale =0;
                    while(1) {
                    mul(&unit_v,scale,&unit_vs);
                    add(&p_l->pos,&unit_vs,&a_v);
                    if(!(a_v.x >=0  && a_v.x < width 
                        && a_v.y >=0 && a_v.y < height
                    )) break;
                    
                     if(antinode[a_v.y][a_v.x]!= 1) {
                            antinode[a_v.y][a_v.x] = 1;
                            cpt ++;
                        }
                        scale += 1;
                    } 
                    a=p_r;
                    b=p_l;
                }

            }
        }
    }
    
    fclose(fp);
    if (line) free(line);
    printf("%lld\n",cpt);
    
}
int main() {

    part_1();
    part_2();
    return 0;
}
