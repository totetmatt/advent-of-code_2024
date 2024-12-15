
#include <stdio.h>
#include "day_13.h"
#define a input[i]
#define b input[i+2]
#define c input[i+1]
#define d input[i+3]
#define e input[i+4]
#define f input[i+5]
#define ee input[i+6]
#define ff input[i+7]
int main() {

    double cpt[2]= {0.0f};
    for(int i=0;i<l_input;i+=8) {
            double det = (a*d)-(b*c);
        {
            double x = ((e*d)-(b*f))/det;
            double y = ((a*f)-(e*c))/det;
            if(x == (int)x && y == (int)y) {
                cpt[0]+= x*3.0f +y;
            }
        }
        {
            double x = ((ee*d)-(b*ff))/det;
            double y = ((a*ff)-(ee*c))/det;
            if(x == ( long)x && y == ( long)y) {
                cpt[1]+= x*3.0f +y;
            }
        }
    }
    printf("%ld\n%ld\n",(long)cpt[0],(long)cpt[1]);
    
}
