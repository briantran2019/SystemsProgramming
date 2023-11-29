import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.mutex = threading.Lock()

def incCount(counter, iterations):
    global finalValue
    with counter.mutex:
        counter.value += iterations
    finalValue = counter.value

def decCount(counter, iterations):
    global finalValue2
    with counter.mutex:
        counter.value -= iterations
    finalValue2 = counter.value

def main():
    counter = Counter()
    iterations = 100000000

    incThreads = [threading.Thread(target=incCount, args=(counter, iterations)) for _ in range(10)]
    decThreads = [threading.Thread(target=decCount, args=(counter, iterations)) for _ in range(10)]

    print(f"Incrementing counter from 0 to {iterations} using 10 threads")
    for thread in incThreads:
        thread.start()
    print(f"Final value is {finalValue}")

    print(f"Incrementing counter from {iterations} to 0 using 10 threads")
    for thread in decThreads:
        thread.start()
    print(f"Final value is {finalValue2}")

    for thread in incThreads + decThreads:
        thread.join()

if __name__ == "__main__":
    main()
