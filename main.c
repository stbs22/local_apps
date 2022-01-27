#include <stdio.h>
#include <stdlib.h>

int main(void){
  char* baka = malloc(4*sizeof(char));
  baka[0] = 'b';
  baka[1] = 'a';
  baka[2] = 'k';
  baka[3] = 'a';
  printf("%s",baka);
  return 0;
}
