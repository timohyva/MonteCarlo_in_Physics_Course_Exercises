#include <math.h>
#include <stdio.h>
#include <float.h>
#include <errno.h>
#include <fenv.h>
#include "mt64.h"
#include <time.h>

//#define kb 8.6173324E-5
//#define T 600.0
//#define n 1E6
#define a 0.2
#define d 10.0
#define A 2.1
//#define DeltaE 0.005 // \DeltaE step length
#define Range_k 500.0 // 100.0-0.0
#define k_Start 0.0 // beginning at 0.0

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

double g(double k)
{
   return (a/(exp(-a*d)))*(exp(-a*(k+d))); // g function for Ag > M-B Distribution
}

double f(double k)
{
   return (pow(3.0,k)*exp(-3))/tgamma(k+1.0); // normlized Maxwell Boltzman Distribution
}

double main(unsigned long long S, unsigned long long N_Points, double Delta_k)
{
  unsigned long long S1,S2,m,e;
  double N,u,k,y,kwsum=0,Wsum=0;
  N=Range_k/Delta_k; // the number of bins corresponding to \Deltak
  double w[(unsigned long long)N];
  for (m=0; m<(unsigned long long)N; m++) {w[m]=0.0;} // weight

  for (m=0; m<N_Points; m++) {
  init_genrand64(S);
  u=genrand64_real2(); // u=P_{u}(0,1)
  S1=genrand64_int64();
  S2=seed_generator(S1);

  k=Gi(u);
  init_genrand64(S2);
  y=A*g(k)*genrand64_real2(); // y=P_{u}(0,Ag(x))
  S=genrand64_int64();

  if (y>f(k)) continue; // Numerical-Analytical Hit-Miss Method
  else {e=(k-k_Start)/Delta_k; w[e]+=1.0;}
  }

  for (m=0; m<N; m++){
      kwsum+=w[m]*(k_Start+((double)m*Delta_k)); // weighted sum of energy
      Wsum+=w[m];
  }

    return kwsum/Wsum; // wighted mean energy in one time runing
}
