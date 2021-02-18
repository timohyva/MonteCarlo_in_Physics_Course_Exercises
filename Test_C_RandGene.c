#include <math.h>
#include <stdio.h>
#include "mt64.h"

#define N_Points 1E1
#define L_Base 2.0
#define L_Shift 1.0
#define L_H 1.0
#define Dim_Base 2.0
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
    unsigned long long S=36127367263,S1;
    int i;
    double x,y,z;
    /*unsigned long long init[4]={0x12345ULL, 0x23456ULL, 0x34567ULL, 0x45678ULL}, length=4;
    init_by_array64(init, length);*/
    /*printf("1000 outputs of genrand64_int64()\n");*/
    /*for (i=0; i<1000; i++) {
      printf("%20llu ", genrand64_int64());
      if (i%5==4) printf("\n");
    }*/
    //printf("\n1000 outputs of genrand64_real2()\n");
    for (i=0; i<N_Points; i++) {
    /*  printf("%10.8f ", genrand64_real2());
      if (i%5==4) printf("\n");*/
    init_genrand64(S);
    //x=(genrand64_real2())*L_Base-L_Shift;
    x=genrand64_real2();
    y=genrand64_real2();
    z=genrand64_real2();
    S1=genrand64_int64();
    //S=(unsigned long long)seed_generator(S1);
    S=seed_generator(S1);
    printf("x=%f y=%f z=%f and S=%20llu\n",x,y,z,S);
    }
    return 0;
}
