from subprocess import Popen as popen, PIPE
import os, time

class CommandRunner():
    def __init__(self) -> None:
        pass

    def run_command(self, cmd: str):
        print(f'\nExecuting command "{cmd}":')
        #split str into list for arg1 of popen
        cmd = cmd.split()
        #use popen to run cmd and assign it to runcmd
        runcmd = popen(cmd, stdout=PIPE, stderr = PIPE, text=True)
        #use commmunicate to capture output of popen and wait subprocess to finish
        cmdout, cmderr = runcmd.communicate()
        #error handling
        if runcmd.returncode != 0:
            print(f"Error: {cmderr}")
        else:
            print(f'Out: {cmdout}')
    
    def parse_ls_output(self):
        #create a txt file to capture ls output into parsable format
        popen(['touch', 'lsout.txt'], stdout=PIPE, text=True)
        #give previous popen extra time to execute
        time.sleep(.1)
        #ls -l current dir and write to txt created earlier
        popen('ls -l > lsout.txt', shell=True, stdout = PIPE)
        #open the txt in read mode
        file = open('lsout.txt', 'r')
        #scan each line
        lines = file.readlines()
        print("Files in current dir are:")
        #iterate through the file
        for line in lines:
            #spilt str of line into list
            linearr = line.split()
            #check if the last entry of ls line contains a . file extension
            if len(linearr) > 7 and '.' in linearr[8]:
                print(f"\t{linearr[8]}")
        print("\r")
