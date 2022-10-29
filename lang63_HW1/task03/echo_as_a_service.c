#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void echo(const char* input)
{
    if (strlen(input) > 100) {
        printf("command is too long\n");
        exit(0);
    }

    char command[150];
    memset(command, 0, 150);
    strcpy(command, "echo \"");
    strcat(command, input);
    strcat(command, "\"");

    setreuid(geteuid(), geteuid());
    system(command);
}

int main(int argc, char** argv)
{
    if (argc <= 1) {
        printf("Usage: I'll print back your input for you :)\n");
        return(0);
    }
    echo(argv[1]);
}