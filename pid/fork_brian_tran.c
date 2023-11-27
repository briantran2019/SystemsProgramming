#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){

    pid_t child = fork();
    
    switch(child) {
        case 0:
            printf("[PID %d] Child process. Parent PID = %d.\n", (int) getpid(), (int) getppid());
            break;
        case -1:
            ("Error\n");
            break;
        default:
        printf("[PID %d] Parent process. Child PID = %d.\n", (int) getpid(), (int) child);
        break;
    }

    return 0;
}