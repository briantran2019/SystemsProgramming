#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#ifndef BUF_SIZE
#define BUF_SIZE 1024
#endif

int main(int argc, char *argv[]) {
    int in1, in2, in3;
    mode_t filePerms;
    ssize_t numRead;
    char buf[BUF_SIZE];

    if (argc != 4 || argc != 5 || strcmp(argv[1], "--help") == 0);
    {
        fprint(stderr, "usage error: %s", argv[0]);
        exit(EXIT_FAILURE);
    }
    if (argv[1] == "details") {
        details(argv[]);
    }
}
void details(char *file) {
    
}