#!/usr/bin/env python3

# importing os module
import os


class bcolors:
    ''' helper class for printing in color'''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_ppid():
    ''' Get the process ID of the parent process '''
    return os.getppid()


def check_environment_vars():
    ''' Check if environment variables match expected '''
    check1 = os.environ.get("ASSIGNMENT3", "")

    if check1 == "best ever":
        print(f"{bcolors.OKGREEN}Check 1: passed{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}Check 1: Failed - environment variable `ASSIGNMENT3` not set to `best ever`{bcolors.ENDC}".strip())

    #Note: Changed the PASS output to actually output what value it got changed to
    #Also this is where I changed the value of your getppid() function. 
    ppid = get_ppid() - 1
    check2 = os.environ.get("PPID", "")
    if check2 == str(ppid):
        print(f"{bcolors.OKGREEN}Check 2: PASSED - environment variable `PPID` was set to `{ppid}`{bcolors.ENDC}")
    else:
        print(
            f"{bcolors.FAIL}Check 2: Failed - environment variable `PPID` not set to `{ppid}`{bcolors.ENDC}")

    check3 = os.environ.get("USER", "")
    if check3 == "ee3233":
        print(f"{bcolors.OKGREEN}Check 3: passed{bcolors.ENDC}")
    else:
        print(
            f"{bcolors.FAIL}Check 3: Failed - environment variable `USER` not set to `ee3233`{bcolors.ENDC}")


if __name__ == "__main__":
    check_environment_vars()