#define _OPEN_SYS_ITOA_EXT
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int solve_1(long *list,size_t size, size_t idx,long current , long r){
    long add = current + list[idx] ;
    long mul = current * list[idx] ; 
    idx++;
    if(idx >= size) {
        return add == r || mul == r;
    }
    return solve_1(list,size,idx,add,r) || solve_1(list,size,idx,mul,r);
}
void part_1() {
FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_07.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

  
;
    while ((read = getline(&line, &len, fp)) != -1) {
            
            long list[20]={0};
            long *p_list = list;
    
            char *result = strtok(line,":");
            long r = atol(result);
            result = strtok(NULL,":");
            result = strtok(result," ");
            while(result!=NULL) {
                *p_list = atol(result);
                p_list++;
                result = strtok(NULL," ");
            }
            size_t list_size = p_list - list;
            cpt+= r *solve_1(list,list_size,1,list[0],r);
           
            
     }

    
    fclose(fp);
    if (line) free(line);
    printf("%lld\n",cpt);
}

int solve_2(long *list,size_t size, size_t idx,long current , long r){
    long add = current + list[idx] ;
    long mul = current * list[idx] ; 
    char a[50];
     char b[50];
     snprintf(a,50,"%ld",current);
     snprintf(b ,50,"%ld",list[idx]);
    strcat(a,b);
    long concat = atol(a);
    idx++;
    if(idx >= size) {
        return add == r || mul == r || concat == r;
    }
    return solve_2(list,size,idx,add,r) || solve_2(list,size,idx,mul,r) || solve_2(list,size,idx,concat,r);
}
void part_2(){  
    FILE * fp;  
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_07.txt";
    long long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

  
;
    while ((read = getline(&line, &len, fp)) != -1) {
            
            long list[20]={0};
            long *p_list = list;
    
            char *result = strtok(line,":");
            long r = atol(result);
            result = strtok(NULL,":");
            result = strtok(result," ");
            while(result!=NULL) {
                *p_list = atol(result);
                p_list++;
                result = strtok(NULL," ");
            }
            size_t list_size = p_list - list;
            cpt+= r *solve_2(list,list_size,1,list[0],r);
           
            
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
