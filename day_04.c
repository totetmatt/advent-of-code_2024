#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h> 
#include <regex.h>   
void print_board(char board[140][140],size_t w,size_t h){
    for(size_t y=0;y<h;y++){
         for(size_t x=0;x<w;x++){
                    printf("%c",board[y][x]); 
         }
          printf("\n");
    }
}
static const char s_p1[3] = {'M','A','S'};
int direction(char board[140][140],size_t w,size_t h,size_t px,size_t py,size_t dx,size_t dy,size_t step) {
    // Can't remember if it 
    //printf("step:%i\n",step);
    if(step>3) return 0;
    if(py+step*dy<0 || py+step*dy>=h ) return 0;
    if(px+step*dx<0 || px+step*dx>=w ) return 0;
    //printf(">> %c == %c \n",board[py+step*dy][px+step*dx],s_p1[step-1]);
    if(board[py+step*dy][px+step*dx] == s_p1[step-1]){
        if(step==3) return 1;
        return direction(board,w,h,px,py,dx,dy,step+1);
    } 
    return 0;
   
}
int direction_2(char board[140][140],size_t w,size_t h,size_t px,size_t py) {
 
    if(px+1 >= w || px-1 <0 || py+1 >= h || py-1 <0 ) return 0;
    char top_left = board[py-1][px-1];
    char top_right= board[py-1][px+1];
    char bot_left = board[py+1][px-1];
    char bot_right = board[py+1][px+1];

    if( top_left != bot_right && (top_left=='M' || top_left=='S' ) && (bot_right=='M' || bot_right=='S' ) 
    && top_right != bot_left && (top_right=='M' || top_right=='S' ) && (bot_left=='M' || bot_left=='S' ) ) {
        return 1;
    }
    return 0;
   
}
void part_1() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_04.txt";

    int cpt = 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    char board[140][140];

    for(size_t y=0;y<140;y++){
         for(size_t x=0;x<140;x++){
             board[y][x]='.';
         }
    }


    size_t height = 0;
    size_t width = 0;
    while ((read = getline(&line, &len, fp)) != -1) {

        memcpy(board[height],line,strlen(line)-1);
        height++;
        width = strlen(line)-1;
    }
   //print_board(board,width,height);
    for(size_t y=0;y<height;y++){
         for(size_t x=0;x<width;x++){
            if(board[y][x]=='X') {

                 /*
                cpt+= direction(board,width,height,x,y,1,0,1);
                cpt+= direction(board,width,height,x,y,0,1,1);
                cpt+= direction(board,width,height,x,y,-1,0,1);
                cpt+= direction(board,width,height,x,y,0,-1,1);

                cpt+= direction(board,width,height,x,y,1,1,1);
                cpt+= direction(board,width,height,x,y,-1,-1,1);

                cpt+= direction(board,width,height,x,y,-1,1,1);
                cpt+= direction(board,width,height,x,y,1,-1,1);
                */
               // Is it better ? I don't know 
                for(int cy= -1;cy<=1;cy++){
                             for(int cx=-1;cx<=1;cx++){ 
                                    cpt+= direction(board,width,height,x,y,cx,cy,1);
                             }
                 }
      
            }
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
    const char * filename ="day_04.txt";

    int cpt = 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    char board[140][140];

    for(size_t y=0;y<140;y++){
         for(size_t x=0;x<140;x++){
             board[y][x]='.';
         }
    }


    size_t height = 0;
    size_t width = 0;
    while ((read = getline(&line, &len, fp)) != -1) {

        memcpy(board[height],line,strlen(line)-1);
        height++;
        width = strlen(line)-1;
    }
    //print_board(board,width,height);
    for(size_t y=0;y<height;y++){
         for(size_t x=0;x<width;x++){
            if(board[y][x]=='A') {
          
                int s = direction_2(board,width,height,x,y);
                 cpt+= s;
                /*if(s == 1){
                    
                    for(int cy= -1;cy<=1;cy++){
                             for(int cx=-1;cx<=1;cx++){ 
                                 printf("%c",board[y+cy][x+cx]);
                             }
                             printf("\n");
                }
                printf("x=%i,y=%i,cpt=%i\n",x,y,cpt);
                }*/
               
                 
      
            }
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

