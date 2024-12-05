#include <stdio.h>
#include <stdlib.h>
#include <string.h>




void part_1() {
FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_05.txt";

    int cpt = 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    int rules[100][100]= {0};
    // Parsing graph
    char *token;
    while ((read = getline(&line, &len, fp)) != -1) {

        if(line[0]=='\n') break;
        token = strtok(line, "|");   
        int source = atoi(token);

        token = strtok(NULL, "|");
        int target = atoi(token);
        rules[source][target] = 1;
        

    }
    // Processing update line
   while ((read = getline(&line, &len, fp)) != -1) {
        int update[100]={0};
        int *p_update=update;
        char *token = strtok(line, ","); 
        while(token!=NULL){
            *p_update = atoi(token);
            p_update++;
            token = strtok(NULL, ",");
        }
        size_t update_size = (p_update-update);
        int is_ok  = 1;
        for(size_t i=0;i<update_size;i++){
            int current = update[i];
            for(size_t j=i+1;j<update_size;j++){
                 is_ok &= rules[current][update[j]];
                
            }
        }
        if(is_ok) {
            cpt += update[update_size/2];
        }
    }
    fclose(fp);
    if (line) free(line);
    printf("%i\n",cpt);
}
void part_2(){    FILE * fp;
   char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_05.txt";

    int cpt = 0;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

    int rules[100][100]= {0};
    // Parsing graph
    char *token;
    while ((read = getline(&line, &len, fp)) != -1) {

        if(line[0]=='\n') break;
        token = strtok(line, "|");   
        int source = atoi(token);

        token = strtok(NULL, "|");
        int target = atoi(token);
        rules[source][target] = 1;
        

    }
    // Processing update line
   while ((read = getline(&line, &len, fp)) != -1) {
        int update[100]={0};
        int *p_update=update;
        char *token = strtok(line, ","); 
        while(token!=NULL){
            *p_update = atoi(token);
        
            p_update++;
            token = strtok(NULL, ",");
        }
        size_t update_size = (p_update-update);
        int is_ok = 1;
      
 
            
            for(size_t i=0;i<update_size;i++){
                int current = update[i];
                for(size_t j=i+1;j<update_size;j++){
                     is_ok &= rules[current][update[j]];
                }
                
            }
            
      
        if(is_ok) {
            continue;
        }
        for(size_t i=0;i<update_size;i++){
          
            do{
                is_ok = 1;   
            size_t max_idx = -1;
            int current = update[i];
            for(size_t j=i+1;j<update_size;j++){
                    int result = rules[current][update[j]];
                    is_ok &=  result;
                    if(result ==0){
                      
                        max_idx = j;
                    }
                    
            }
            if(max_idx != -1){
               
                int tmp = update[i];
                update[i] = update[max_idx];
                update[max_idx] = tmp;
            }
            } while(is_ok==0);
        }
        cpt += update[update_size/2];
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
