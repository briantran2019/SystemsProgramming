#include <signal.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void signal_handler(int signum) { 
    printf("This is a signal handler!\n");
}

void signal_handler_parent(int signum) {
    printf("Parent started... \n");
    sleep(3);
    printf("Parent about to signal child\n");
}

int main () {
    int how = SIG_BLOCK;
    sigset_t sigusr = SIGUSR1;
    sigset_t* oldset = NULL;
    sigprocmask(how, &sigusr, oldset);

    signal(SIGUSR1, signal_handler);
    raise(SIGUSR1);

    pid_t pid = fork();

    if (pid < 0) {
        printf("fork() error\n");
        exit(1);
    }
    else if (pid != 0) {
        signal(SIGUSR1, signal_handler_parent);
    }
    /* pid_t p = fork();
    if(p<0){
      perror("fork fail");
      exit(1);
    }
    printf("Hello world!, process_id(pid) = %d \n", getpid());
    printf("PPID: %d \n", getppid()); */
    return 0;
}