#include "mysecret.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_hash(const char* user_input)
{
    // Limit char set
    for (int i = 0; i < SECRET_LEN; i++) {
        if (user_input[i] < 'A' || user_input[i] > 'Z') {
            printf("Out of range\n");
            exit(0);
        }
    }

    char command[100];
    strcpy(command, "echo -n ");
    strcat(command, user_input);
    strcat(command, " | md5sum | awk '{print $1}'");

    FILE *fp = popen(command, "r");

    char c;
    char hash[33];
    for (int i = 0; i < 32; i++) {
        fread(&c, 1, 1, fp);
        hash[i] = c;
    }
    hash[32] = '\0';
    pclose(fp);

    // Slightly increased chance of a hash collision
    if (strncmp(hash, SECRET, SECRET_LEN) == 0) {
        return(1);
    } else {
        return(0);
    }
}

int main(int argc, char** argv)
{
    char user_input[SECRET_LEN+1];

    if (argc <= 1) {
        printf("You have to give me an input silly ;)\n");
        return(0);
    } else if (strlen(argv[1]) != SECRET_LEN) {
        printf("Check your input, its the wrong size\n");
    } else {
        strncpy(user_input, argv[1], SECRET_LEN + 1);

        if (check_hash(user_input)) {
            printf("Success!\n");
            FILE *fp = fopen("flag.txt", "r");
            if (fp == NULL) {
                printf("Error flag is not found. Contact the TA");
            }

            char c;
            while (fread(&c, 1, 1, fp)) {
                printf("%c", c);
            }
            fclose(fp);
        } else {
            printf("Keep trying, I believe in you\n");
        }
        return(0);
    }
}