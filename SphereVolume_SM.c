#include <math.h>
#include <stdio.h>
#include "mt64.h"

#define N_Points 9E7
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
    double r,xi[Dim_Base],sxi2=0.0,z,sumz=0.0,V_M,V_Mn1=L_Base*L_Base;
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


        if (sxi2<1) {z=sqrt(1-sxi2); sumz+=z; l++;} //printf("xi0 %10.8f, xi1 %10.8f less than %10.8f\n",xi[0],xi[1],sxi2);}
        else ;//printf("larger than 1: xi0 %10.8f, xi1 %10.8f and %10.8f\n",xi[0],xi[1],sxi2);

    }

    r=sumz/n;
    V_M=V_Mn1*(2*r);
    printf("sumz/n %10.8f, sumz %10.8f and n %llu",r,sumz,n);
    printf("volume of %lu-sphere is: %10.8f\n",Dim_Sphere,V_M);
    printf("V_Mn1 is %10.8f\n",V_Mn1);
    return 0;
}
