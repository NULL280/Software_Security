#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cat_file(const char* input_file)
{
    // Limit char set
    for (int i = 0; i < strlen(input_file); i++) {
        if (input_file[i] == 'f' ||
                input_file[i] == 'l' ||
                input_file[i] == 'a' ||
                input_file[i] == 'g'
                ) {
            printf("Permission denied\n");
            exit(0);
        }
    }

    FILE *fp = fopen(input_file, "r");
    if (fp == NULL) {
        printf("Error opening file");
    }

    char c;
    while (fread(&c, 1, 1, fp)) {
        printf("%c", c);
    }
    fclose(fp);
}

int main(int argc, char** argv)
{
    if (argc <= 1) {
        printf("Usage: give me a file to print\n");
        return(0);
    }
    cat_file(argv[1]);
}