#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void part_1() {
        FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_02.txt";
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    

    int counter = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        int list [10] = {0};
        int *plist = list;
        char *token = strtok(line, " ");   
        while(token != NULL) {

            int val = atoi(token);
            *plist = val;
            plist++; 
            token = strtok(NULL, " ");
        }

        size_t list_size = (size_t)(plist-list);
       
        int slope = (list[0] - list[1])/ abs(list[0] - list[1]);
        int safe = 1;
        for(size_t i=0;i<list_size-1;i++){
            int delta = list[i]-list[i+1];
            if(abs(delta) >3  || delta/abs(delta) != slope) { safe=0;break;}
     
        }
       
        counter += safe;
     
    }

    fclose(fp);
    if (line) free(line);
    
    printf("%i\n",counter);
   
}
void part_2() {
      FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_02.txt";
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    

    int counter = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        int list [10] = {0};
        int *plist = list;
        char *token = strtok(line, " ");   
        while(token != NULL) {

            int val = atoi(token);
            *plist = val;
            plist++; 
            token = strtok(NULL, " ");
        }

        size_t list_size = (size_t)(plist-list);
        for(size_t i=0;i<list_size;i++){
            int sublist[10]= {0};
            int *psublist = sublist;
            for(size_t j=0;j<list_size;j++){
                if(i==j) continue;
               
                *psublist = list[j];
                psublist++;
            }
            size_t sublist_size = (size_t)(psublist-sublist);
          
            int slope = (sublist[0] - sublist[1])/ abs(sublist[0] - sublist[1]);
            int safe = 1;
            for(size_t i=0;i<sublist_size-1;i++){
                int delta = sublist[i]-sublist[i+1];
                if(abs(delta) >3  || delta/abs(delta) != slope) { safe=0;break;}
        
            }
            if(safe){
             counter += safe;
             break;
             }
        }
        
        
        
     
    }

    fclose(fp);
    if (line) free(line);
    
    printf("%i\n",counter);
}
int main() {
    part_1();
    part_2();
    return 0;
}