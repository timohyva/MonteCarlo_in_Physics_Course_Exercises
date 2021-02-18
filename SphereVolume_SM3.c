#include <math.h>
#include <stdio.h>
#include "mt64.h"

//#define N_Points 9E3
#define L_Base 2.0
#define L_Shift 1.0
#define L_H 1.0
//#define Dim_Base 2

//int main(void)

unsigned long long seed_generator(unsigned long long seed)
{
   unsigned long long aaa;
   init_genrand64(seed);
   aaa=genrand64_int64();
   return aaa;
 }

double main(double N_Points, double V_Mn1, unsigned int Dim_Base)
{
    unsigned long long S=36127367263,S1,n,k,l=0;
    //unsigned int Dim_Base;
    //double r,xi[Dim_Base],sxi2=0.0,z,z2,zbar,z2bar,sigma_Vbar,sumz=0.0,sumz2=0.0,V_M,V_Mn1,N_Points;
    double r,xi[Dim_Base],sxi2=0.0,z,z2,zbar,z2bar,sigma_Vbar,sumz=0.0,sumz2=0.0,V_M;

    for (n=0; n<N_Points; n++) {
    sxi2=0;

        for (k=0; k<Dim_Base; k++) {
        init_genrand64(S);
        xi[k]=(genrand64_real2())*L_Base-L_Shift;
        S1=genrand64_int64();
        S=seed_generator(S1);

        sxi2=sxi2+xi[k]*xi[k];
        }

        if (sxi2<1) {z2=1-sxi2; z=sqrt(1-sxi2); sumz2+=z2; sumz+=z; l++;}
        else ;

    }

    zbar=sumz/l;
    z2bar=sumz2/l;
    V_M=2*V_Mn1*(zbar);
    sigma_Vbar=V_Mn1*(sqrt((z2bar-zbar*zbar)/n));

    printf("volume of %u-sphere in sampling method is: %10.8f\n",Dim_Base,V_M);
    printf("with error of mean %10.8f",sigma_Vbar);
    printf(" and %llu points\n",l);
    return V_M;
}
