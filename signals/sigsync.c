#include <signal.h>
#include <stdio.h>

int main () {
    int how = SIG_BLOCK;
    sigset_t sigusr = SIGUSR1;
    int* oldset = NULL;
    sigprocmask(how, sigusr, oldset);
    



    return 0;
}