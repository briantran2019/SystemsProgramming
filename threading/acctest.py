import threading, os, sys


def func2(startdir, strToFind):
    for (thisDir, dirsHere, filesHere) in os.walk(startdir):
        for fname in filesHere:
            fpath = os.path.join(thisDir, fname)
            if strToFind in open(fpath).read():
                print(fpath)

func2(sys.argv[1], "123456")