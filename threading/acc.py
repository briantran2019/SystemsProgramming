import threading

glist = []
for i in range(500):
    glist.append(i)

alist = [0,0,0,0,0]

def accumulate(start):
    global alist
    acc = 0
    i = glist[start * 100]   
    j = glist[i + 99]

    for num in range(i, j + 1):
        acc += num
    
    alist[start] = acc
    tid = threading.get_native_id()
    print(f"Accumulated value in thread [{tid} -> {start}] is {acc}")

def startOrJoinThreads(threadlist, start):
    if(start):
        for thread in threadlist:
            thread.start()
    else:
        for thread in threadlist:
            thread.join()

def main():
    t0 = threading.Thread(target=accumulate, args=((0),))
    t1 = threading.Thread(target=accumulate, args=((1),))
    t2 = threading.Thread(target=accumulate, args=((2),))
    t3 = threading.Thread(target=accumulate, args=((3),))
    t4 = threading.Thread(target=accumulate, args=((4),))
    threadList = [t0, t1, t2, t3, t4]
    startOrJoinThreads(threadList, t0)
    print(f"Total: {sum(alist)}")

if __name__ == "__main__":
    main()