#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>

void signal_handler(int signum) { 
    printf("This is a signal handler!\n");
}

void signal_handler_parent(int signum) {
}

void signal_handler_child(int signum) {
}

int main () {
    int how = SIG_BLOCK;
    sigset_t sigusr = SIGUSR1;
    sigset_t* oldset = NULL;
    sigset_t emptyset, origset;
    sigprocmask(how, &sigusr, oldset);

    signal(SIGUSR1, signal_handler);
    raise(SIGUSR1);

    pid_t pid = fork();

    if (pid < 0) {
        printf("fork() error\n");
        exit(EXIT_FAILURE);
    }
    else if (pid != 0) {
        //signal(SIGUSR1, signal_handler_parent);
        printf("Parent started... \n");
        sleep(3);
        printf("Parent about to signal child\n");
        signal(SIGUSR1, signal_handler_child);
        exit(EXIT_SUCCESS);
    }
    else {
        //signal(SIGUSR1, signal_handler_child);
        sigemptyset(&emptyset);
        if (sigprocmask(SIG_SETMASK, &origset, NULL) == -1) {
            perror("sigprocmask");
            exit(EXIT_FAILURE);
        }
        exit(EXIT_SUCCESS);
    }
    return 0;
}