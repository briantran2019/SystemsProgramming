#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#ifndef BUF_SIZE
#define BUF_SIZE 1024
#endif
int main(int argc, char *argv[])
{
    int inputFd, outputFd1, outputFd2, openFlags;
    mode_t filePerms;
    ssize_t numRead;
    char buf[BUF_SIZE];

    //needs 4 arguments
    if (argc != 4 || strcmp(argv[1], "--help") == 0)
    {
        fprintf(stderr, "usage error: %s old-file new-file\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    /* Open input and output files */
    inputFd = open(argv[1], O_RDONLY); /* O_CREAT is not specified, mode can be omitted */
    if (inputFd == -1)
    {
        fprintf(stderr, "Opening Error!: %s \n", argv[1]);
        exit(EXIT_FAILURE);
    }

    openFlags = O_CREAT | O_WRONLY | O_TRUNC;
    filePerms = S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH; /* rw-rw-rw- */
    outputFd1 = open(argv[2], openFlags, filePerms);
    if (outputFd1 == -1) /* If an error occurs, open returns -1 */
    {
        fprintf(stderr, "Opening Error!: %s \n", argv[2]);
        exit(EXIT_FAILURE);
    }

    //new Fd for second destination file which is index 3 of the cmd line argument vector
    outputFd2 = open(argv[3], openFlags, filePerms);
    if (outputFd2 == -1)
    {
        fprintf(stderr, "Opening Error!: %s \n", argv[3]);
        exit(EXIT_FAILURE);
    }

    /* Transfer data until we encounter end of input or an error */
    while ((numRead = read(inputFd, buf, BUF_SIZE)) > 0)
        //needed to add extra condition for if for second destination file
        if (write(outputFd1, buf, numRead) && write(outputFd2, buf, numRead) != numRead)
        {
            fprintf(stderr, "couldn't write whole buffer");
            exit(EXIT_FAILURE);
        }
    if (numRead == -1)
    {
        fprintf(stderr, "read");
        exit(EXIT_FAILURE);
    }
    if (close(inputFd) == -1)
    {
        fprintf(stderr, "close input");
        exit(EXIT_FAILURE);
    }
    if (close(outputFd1) == -1)
    {
        fprintf(stderr, "close output");
        exit(EXIT_FAILURE);
    }
    if (close(outputFd2) == -1)
    {
        fprintf(stderr, "close output");
        exit(EXIT_FAILURE);
    }
    exit(EXIT_SUCCESS);
}