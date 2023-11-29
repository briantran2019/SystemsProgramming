import subprocess, os, time, sys

#Always make the working directory the one the script is in at runtime
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

time.sleep(0.01)

str1 = str(sys.argv[1])
str2 = str(sys.argv[2])

print("Using Popen to echo '" + str1 + "' to a file")
subprocess.Popen("echo " + str1 + " >> " + str2, shell=True)

print("Using Popen to cat " + str2)
cat = subprocess.Popen("cat " + str2, shell=True, stdout=subprocess.PIPE)
catout = cat.communicate()[0]
print(f"{str2} contains '{catout.decode('UTF-8')}'")