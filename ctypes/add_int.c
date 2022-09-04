/**************************************
Compile with:
$ gcc -shared -Wl,-soname,add_int -o add_int.so -fPIC add_int.c
***************************************/

#include <stdio.h>

int add(int a, int b)
{
  return a+b;
}
