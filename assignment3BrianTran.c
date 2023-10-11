#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void check_code();

int main()
{
    static char *newstr = "ASSIGNMENT3=best ever"; //create string to set new name
    putenv(newstr); //put new name

    pid_t pid = getpid(); //get the pid and set to the integer pid
    char pid_str[11] = {0}; //declare empty array called pid_str to put pid in
    sprintf(pid_str, "PPID=%d", pid); //concatenate pid to PPID=
    putenv(pid_str); //put pid_str as ppid
    
    static char *userenv = "USER=ee3233"; //declare new user string
    putenv(userenv); //put new name
    check_code();

    return 0;
}

void check_code()
{
    system("python3 check_env.py");
    sleep(1);
}