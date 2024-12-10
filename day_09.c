#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/*

00...111...2...333.44.5555.6666.777.888899
0123456
{0>0,2}
{1>5:3}

*/
struct Node {
    char id[10];
    long start;
    long size;
    long end;
    struct Node* next;
} Node;
void part_1() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_09.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    long size=0;
    long list[100000] = {-1};
    long *p_list=list;
    while ((read = getline(&line, &len, fp)) != -1) {
            

            size = strlen(line);
            for(long i=0;i<size;i++){
                long size= line[i]-48;
                if(i%2==0){ // File
                    long id = i/2;
                    
                    for(long s=0;s<size;s++){

                            *p_list=id;
                            p_list++;
                    }
                   
                  
                } else { // Free
                   for(long s=0;s<size;s++){
                            *p_list=-1;
                            p_list++;
                    }
                }
            }

            size_t s_list = p_list-list;
            /*for(size_t i=0;i<s_list;i++){
                if(list[i]==-1) {
                    printf(".");
                } else {
                 printf("%ld",list[i]);
                }

            }*/

            long *l_ptr = list;
            long *r_ptr = p_list-1;

            while(l_ptr <= r_ptr) {
                if(*l_ptr!=-1) {
                    l_ptr++;
                    continue;
                }
                if(*r_ptr==-1){
                    r_ptr--;
                    continue;
                }
                long tmp = *r_ptr;
                *r_ptr = *l_ptr;
                *l_ptr = tmp;
                r_ptr--;
                l_ptr++;
            }
   
            for(size_t i=0;i<s_list;i++){
                if(list[i]==-1) {
                    continue;
                } else {
                 cpt += list[i]*i;
                }

            }
    }
    
  
    fclose(fp);
    if (line) free(line);
    printf("%ld\n",cpt);
}
void part_2(){  
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_09.test.txt";
    long cpt= 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    long size=0;
    long list[100000] = {-1};
    long *p_list=list;
    while ((read = getline(&line, &len, fp)) != -1) {
            

            size = strlen(line);
            for(long i=0;i<size;i++){
                long size= line[i]-48;
                if(i%2==0){ // File
                    long id = i/2;
                    
                    for(long s=0;s<size;s++){

                            *p_list=id;
                            p_list++;
                    }
                   
                  
                } else { // Free
                   for(long s=0;s<size;s++){
                            *p_list=-1;
                            p_list++;
                    }
                }
            }

            size_t s_list = p_list-list;
            
            printf("\n");
            for(size_t i=0;i<s_list;i++){
                if(list[i]==-1) {
                    printf(".");
                } else {
                 printf("%ld",list[i]);
                }

            }
            printf("\n");
            long *p_file_s = p_list-1;
            long *p_file_e = p_file_s;
            while(p_file_s>=list) {
                long *p_free_s = list;
                long *p_free_e = list;
                // as long as we are at the left side of the file
                while(p_free_s < p_file_s) {
                    // Find first free 
                    while(*p_free_s!=-1){
                        *p_free_s++;
                    }
                    
                    p_free_e = p_free_s;
                    while(*p_free_e==-1){
                        *p_free_e++;
                    }
                    p_free_e--;
                    printf("%zu %zu %zu\n",p_free_s,p_free_e,p_free_e-p_free_s+1 );
                    // Find file
                    while(*p_file_s==*p_file_e) {
                        *p_file_s--;
                    }
                    p_file_s++;
                    long filesize = p_file_e-p_file_s+1 ;
                    printf("%zu %zu %zu",p_file_s,p_file_e,filesize);

                    if(filesize <= p_free_e-p_free_s+1 ) {
                        long buf[1000]= {0};
                        memcpy(buf,p_free_s,filesize*sizeof(long));
                        memcpy(p_free_s,p_file_s,filesize*sizeof(long));
                        memcpy(p_file_s,buf,filesize*sizeof(long));
           
                        break;
                    }
    

                }
                p_file_s--;
                p_file_e=p_file_s;
                
                printf("\n");
            }
            printf("\n");
            for(size_t i=0;i<s_list;i++){
                if(list[i]==-1) {
                    printf(".");
                } else {
                 printf("%ld",list[i]);
                }

            }
            printf("\n");
            for(size_t i=0;i<s_list;i++){
                if(list[i]==-1) {
                    continue;
                } else {
                 cpt += list[i]*i;
                }

            }
           
            printf("\n");
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
