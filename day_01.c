#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int int_cmp ( const void * l, const void * r ) {
    int a = * (const int *) l;
    int b = * (const int *) r;
    return a - b;
}
void part_1() {
        FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_01.txt";
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    int list [2][1000] = {0};
    int *l_list = list[0];
    int *r_list = list[1];
    
    while ((read = getline(&line, &len, fp)) != -1) {
        char *token = strtok(line, "   ");
        int val = atoi(token);

        *l_list = val;
        l_list++;            

        token = strtok(NULL, "   ");
        val = atoi(token);

        *r_list = val;
        r_list++;  
    }

    fclose(fp);
    if (line) free(line);
    

   
    qsort(list[0],l_list-list[0],sizeof(int),int_cmp);
    qsort(list[1],r_list-list[1],sizeof(int),int_cmp);   
    int result = 0;
    for(size_t i = 0; i<(size_t)(l_list-list[0]);i++) {
        result += abs(list[0][i]-list[1][i]);
    }
    printf("%i\n",result);
}
void part_2() {
        FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_01.txt";
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);
    
    int list [2][99999] = {0};
    int *l_list = list[0];
    
    while ((read = getline(&line, &len, fp)) != -1) {
        char *token = strtok(line, "   ");
        int val = atoi(token);

        *l_list = val;
        l_list++;            

        token = strtok(NULL, "   ");
        size_t idx = (size_t)atoi(token);
        list[1][idx]++;
    }

    fclose(fp);
    if (line) free(line);
    

    int result = 0;
    for(size_t i = 0; i<(size_t)(l_list-list[0]);i++) {
        int el = list[0][i];
        result += el*list[1][el];
    }
    printf("%i\n",result);
}
int main() {
    part_1();
    part_2();
    return 0;
}