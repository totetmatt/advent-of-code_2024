#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
long reg[3];
long *a = &reg[0];
long *b = &reg[1];
long *c = &reg[2];

int prg[16] = {0};
int out[16] = {0};
int *p_out = out;
long combo(long val) {
    if(val<=3) return val;
    if(val==4) return *a;
    if(val==5) return *b;
    if(val==6) return *c;
}
int main(int argc,char** argv) {
    
    *a = atol(argv[1]);
    *b = atol(argv[2]);
    *c = atol(argv[3]);

    int *sp = prg ;
    char *c = strtok(argv[4],",");

    while(c!=0) {
        *sp = atoi(c);
        c = strtok(NULL,",");
        sp++;
    }

   

    sp = prg;
    int cc = 0;
    while(sp<prg+15 && cc < 16) {
           cc++;
        printf("A=%i,B=%i,C=%i \n",reg[0],reg[1],reg[2]);
        printf("start=%zu,sp=%zu,end=%zu\n",prg,sp,prg+16);
        printf("Op:%i\n",*sp);
        switch(*sp) {
            case 0: *a= *a / pow(2,combo(*(sp+1)));
                    sp+=2;
                    break;
            case 1: *b=*b ^*(sp+1);
                    sp+=2;
                    break;
            case 2: *b=combo(*(sp+1))%8;
                    sp+=2;
                    break;
            case 3: if(*a==0) {sp+=2;}else{sp=prg+(*(sp+1));};
                    break;
            case 4: *b=*b^*c;
                    sp+=2;
                    break;
            case 5: *p_out = *a%8;
                    p_out++;
                    sp+=2;
                    break;
            case 6: *b= *a / pow(2,combo(*(sp+1)));
                    sp+=2;
                    break;            
            case 7: *c= *a / pow(2,combo(*(sp+1)));
                printf("LOUT");
                    sp+=2;
                    break;
                  
        }
    }
    


}