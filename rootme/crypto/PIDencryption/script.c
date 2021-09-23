#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <crypt.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[]){
char pid[16];
char encrypted[50];
snprintf(pid, sizeof(pid), "%i", getpid());

fprintf(stdout,"Your pid is %s", pid);
snprintf(encrypted, sizeof(encrypted), "%s", crypt(pid, "$1$awesome"));
fprintf(stdout, "Encrypted is %s", encrypted);


return 0;
}
