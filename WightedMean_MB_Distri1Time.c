#include <math.h>
#include <stdio.h>
#include <float.h>
#include <errno.h>
#include <fenv.h>
#include "mt64.h"
#include <time.h>

#define kb 8.6173324E-5
#define T 600.0
#define n 1E6
#define a 9.090909091
#define d 10.0
#define A 1.5
#define PI 3.14159265358979323846
//#define DeltaE 0.005 // \DeltaE step length
#define Range_E 50.0 // 100.0-0.0
#define E_Start 0.0 // beginning at 0.0

unsigned long long seed_generator(unsigned long long seed)
{
   unsigned long long aaa;
   init_genrand64(seed);
   aaa=genrand64_int64();
   return aaa;
 }

double Gi(double u)
{
   return (log(1/(1-u)))/a; // x=G^{-1}(u);
}

double g(double e)
{
   return (a/(exp(-a*d)))*(exp(-a*(e+d))); // g function for Ag > M-B Distribution
}

double MB_f(double e)
{
   double norm,c,b;
   c=(2/sqrt(PI))*(n/pow((kb*T),1.5));
   b=kb*T;
   norm=1/(0.5*pow(b,1.5)*c*sqrt(PI));

   return norm*c*sqrt(e)*exp(-e/b); // normlized Maxwell Boltzman Distribution
}

double main(unsigned long long S, unsigned long long N_Points, double DeltaE)
{
  unsigned long long S1,S2,m,k;
  double N,u,e,y,Esum=0,Wsum=0;

  N=Range_E/DeltaE; // the number of bins corresponding to \DeltaE
  double w[(unsigned long long)N];
  for (m=0; m<(unsigned long long)N; m++) {w[m]=0.0;} // weight

  for (m=0; m<N_Points; m++) {
  init_genrand64(S);
  u=genrand64_real2(); // u=P_{u}(0,1)
  S1=genrand64_int64();
  S2=seed_generator(S1);

  e=Gi(u);
  init_genrand64(S2);
  y=A*g(e)*genrand64_real2(); // y=P_{u}(0,Ag(x))
  S=genrand64_int64();

  if (y>MB_f(e)) continue; // Numerical-Analytical Hit-Miss Method
  else {k=(e-E_Start)/DeltaE; w[k]+=1.0;}
  }

  for (m=0; m<N; m++){
      Esum+=w[m]*(E_Start+((double)m*DeltaE)); // weighted sum of energy
      Wsum+=w[m];
  }

    return Esum/Wsum; // wighted mean energy in one time runing
}
