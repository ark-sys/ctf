#include <stdio.h>

void FUN_0804851c(unsigned char *param_1, char *param_2)

{
    unsigned char *pbVar1;
    unsigned char bVar2;
    unsigned char *pbVar3;
    int iVar4;

    *param_1 = *param_1 ^ 0xab;
    pbVar3 = param_1 + 1;
    bVar2 = *pbVar3;
    if (bVar2 != 0) {
        iVar4 = 1;
        do {
            bVar2 = bVar2 - (char)iVar4;
            *pbVar3 = bVar2;
            pbVar1 = param_1 + iVar4 + -1;
            bVar2 = bVar2 ^ *pbVar1;
            *pbVar3 = bVar2;
            bVar2 = bVar2 + *pbVar1;
            *pbVar3 = bVar2;
            bVar2 = bVar2 ^ *pbVar1;
            *pbVar3 = bVar2;
            bVar2 = bVar2 ^ param_1[8];
            *pbVar3 = bVar2;
            if (bVar2 == 0) {
                *pbVar3 = 1;
            }
            iVar4 = iVar4 + 1;
            pbVar3 = param_1 + iVar4;
            bVar2 = param_1[iVar4];
        } while (bVar2 != 0);
    }
    bVar2 = *param_1;
    while (bVar2 != 0) {
        snprintf(param_2, 100,"%.2x", (unsigned int)bVar2);
        param_2 = param_2 + 2;
        param_1 = param_1 + 1;
        bVar2 = *param_1;
    }
//    return;
}


int main()
{
    char flag_buffer[4096];
    unsigned char key[100] = "THEPASSWORDISEASYTOCRACK";
    FUN_0804851c(key, flag_buffer);
    printf("password is : %s", flag_buffer);

    return 0;
}

