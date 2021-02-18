#include <math.h>
#include <stdio.h>
#include "mt64.h"

#define N_Points 9E3
#define L_Base 2.0
#define L_Shift 1.0
#define L_H 1.0
#define Dim_Base 2
#define Dim_Sphere 2lu
//int main(void)

unsigned long long seed_generator(unsigned long long seed)
{
   unsigned long long aaa;
   init_genrand64(seed);
   aaa=genrand64_int64();
   return aaa;
 }

double main()
{
    unsigned long long S=36127367263,S1,n,k,l=0;
    //int n,k;
    double r,xi[Dim_Base],sxi2=0.0,z,z2,zbar,z2bar,sigma_Vbar,sumz=0.0,sumz2=0.0,V_M,V_Mn1=L_Base*L_Base;
    //double r,xi[Dim_Base],sxi2=0.0,z,sumz=0.0,V_M,V_Mn1=3.1415926;

    /*unsigned long long init[4]={0x12345ULL, 0x23456ULL, 0x34567ULL, 0x45678ULL}, length=4;
    init_by_array64(init, length);*/
    /*printf("1000 outputs of genrand64_int64()\n");*/
    /*for (i=0; i<1000; i++) {
      printf("%20llu ", genrand64_int64());
      if (i%5==4) printf("\n");
    }*/
    //printf("\n1000 outputs of genrand64_real2()\n");
    for (n=0; n<N_Points; n++) {
    /*  printf("%10.8f ", genrand64_real2());
      if (i%5==4) printf("\n");*/
    sxi2=0;

        for (k=0; k<Dim_Base; k++) {
        init_genrand64(S);
        xi[k]=(genrand64_real2())*L_Base-L_Shift;
        S1=genrand64_int64();
        S=seed_generator(S1);

        sxi2=sxi2+xi[k]*xi[k];
        }
    //printf("xi0 %f, xi1 %f and %f\n",xi[0],xi[1],sxi2);


        if (sxi2<1) {z2=1-sxi2; z=sqrt(1-sxi2); sumz2+=z2; sumz+=z; l++;} //printf("xi0 %10.8f, xi1 %10.8f less than %10.8f\n",xi[0],xi[1],sxi2);}
        else ;//printf("larger than 1: xi0 %10.8f, xi1 %10.8f and %10.8f\n",xi[0],xi[1],sxi2);

    }

    zbar=sumz/n;
    z2bar=sumz2/n;
    V_M=2*V_Mn1*(zbar);
    sigma_Vbar=V_Mn1*(sqrt((z2bar-zbar*zbar)/n));

    printf("volume of %u-sphere in sampling method is: %10.8f\n",Dim_Base,V_M);
    printf("with error of mean %10.8f",sigma_Vbar);
    printf("and %10.8f\n",N_Points);
    return 0;
}
