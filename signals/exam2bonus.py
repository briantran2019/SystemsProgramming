#does not work

import os

pid_max = 500000

child = os.fork()

if child == 0: 
    with open("/proc/sys/kernel/pid_max", "r") as file:
        pid_max = int(file.read())
    print("Child: Old pid_max = " + str(pid_max))
    
    with open("/proc/sys/kernel/pid_max", "w") as file:
        file.write(str(pid_max))
    print("Child: pid_max now = " + str(pid_max))

else:
    status = os.wait()

    if os.WIFEXITED(status):
        with open("/proc/sys/kernel/pix_max", "r") as file:
            pid_max = int(file.read())
        print("Parent: New pid_max = " + str(pid_max))
    else:
        print("Parent: Child process exit error")