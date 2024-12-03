#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h> 
#include <regex.h>   
void part_1() {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_03.txt";
    regex_t regex;
   
    int cpt = 0;


    int reg_ret = regcomp(&regex, "mul\\(([0-9]+),([0-9]+)\\)", REG_EXTENDED);
    if(reg_ret) exit(1);

    size_t ngroups = regex.re_nsub + 1;
    regmatch_t *groups = malloc(ngroups * sizeof(regmatch_t));

    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);
     char *s;
    while ((read = getline(&line, &len, fp)) != -1) {
        s= line;
        while(regexec(&regex, s, ngroups, groups, 0)==0){
            char buf[10]={0};
            int mul_val = 1.;
            // Groups
            for(size_t i=1;i<ngroups;i++){
                size_t start = groups[i].rm_so;
                size_t length = groups[i].rm_eo- groups[i].rm_so;
                memcpy(buf,s+start,length);
                buf[length]='\0';
                mul_val *= atoi(buf);
            }
            cpt += mul_val;
            s += groups[0].rm_eo;
        }
    }
    fclose(fp);
    if (line) free(line);
    regfree(&regex);
    printf("%i\n",cpt);
}
void part_2(){
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    const char * filename ="day_03.txt";
    regex_t regex;
   
    int cpt = 0;


    int reg_ret = regcomp(&regex, "mul\\(([0-9]+),([0-9]+)\\)|don't\\(\\)|do\\(\\)", REG_EXTENDED);
    if(reg_ret) exit(1);

    size_t ngroups = regex.re_nsub + 1;
    regmatch_t *groups = malloc(ngroups * sizeof(regmatch_t));
    int activate =1;
    fp = fopen(filename, "r");
    if (fp == NULL) exit(EXIT_FAILURE);

     char *s;
    while ((read = getline(&line, &len, fp)) != -1) {
       
        s= line;
        while(regexec(&regex, s, ngroups, groups, 0)==0){
            char buf[20]={0};
            int mul_val = 1.;
            // Groups
            size_t start = groups[0].rm_so;
            size_t length = groups[0].rm_eo- groups[0].rm_so;
            memcpy(buf,s+start,length);
            buf[length]='\0';
            if(strcmp(buf,"do()")==0) activate = 1;
            if(strcmp(buf,"don't()")==0) activate = 0;
            if(activate==1){
                for(size_t i=1;i<ngroups ;i++ ){
                    size_t start = groups[i].rm_so;
                    size_t length = groups[i].rm_eo- groups[i].rm_so;
                    memcpy(buf,s+start,length);
                    buf[length]='\0';
                    mul_val *= atoi(buf);
                }
                cpt += mul_val;
            }
            s += groups[0].rm_eo;
        }
    }
    fclose(fp);
    if (line) free(line);
    regfree(&regex);
    printf("%i\n",cpt);
}
int main() {
    part_1();
    part_2();
    return 0;
}