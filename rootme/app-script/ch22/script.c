#include <unistd.h>


int main(int argc, char **argv){
    char *arg[] = { "/bin/bash", "-p", "/mnt/d/OneDrive/CTF/rootme/app-script/ch22/ch22.sh", argv[1] , NULL };
    execve(arg[0], arg, NULL);
return 0;
}
