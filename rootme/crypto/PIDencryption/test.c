#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <crypt.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[]){
  char pid[16];
  char encrypted[20];
  char test[100];	
  char res[50];  

  if(argc<1){
	fprintf(stderr,"Usage, ./test [pass]");
	return 1;

  }
  snprintf(test, sizeof(test), argv[1]);
  for(int i = 0 ; i < 10000 ; i++){
  snprintf(pid,sizeof(pid),"%i",i);
  snprintf(res, sizeof(res),crypt(pid,"$1$awesome"));
  if(strcmp(test,res)==0){
  printf("PID is %s and encrypted is %s\n",pid, res);
  return 0;
  }
  }
return 1;
}
