#include <stdio.h>
#include "mt64.h"

unsigned long long main(unsigned long long S)
{
   init_genrand64(S);
   init_genrand64(genrand64_int64());
   init_genrand64(genrand64_int64());
   return genrand64_int64();
}
