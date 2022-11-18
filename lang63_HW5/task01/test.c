#include <stdio.h>
int main() {
    unsigned short a = -1;
    printf("cat to short: %d\n", (short) a);
    printf("cat to ulong: %ld\n", (unsigned long) a);
    return 0;
}