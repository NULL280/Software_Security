#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

static const long int a = 65539;
static const long int c = 4282663;
static long int state = 0;

void seed(int seedvalue)
{
    state = seedvalue;
}

long int get_rand()
{
    state = state * a + c;
    return(state);
}

int main(int argc, char**argv)
{
    seed(time(0) - 20);

    long int lotto = get_rand();
    long result;

    if (argc == 2) {
        result = atol(argv[1]);
    } else {
        exit(1);
    }

    if (result == lotto) {
        printf("you win!!!\n");
        setreuid(geteuid(), geteuid());
        system("cat flag.txt");
    } else {
        printf("Fail\n");
    }
}