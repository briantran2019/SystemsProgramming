import time

start = time.time()
def fibrecursive(n):
    if n < 2:
        return n
    return fibrecursive(n - 1) + fibrecursive(n - 2)
fibrecursive(40)
end = time.time()
ntime = end - start
print("Naive Time: " + str("{:.2f}".format(ntime)) + "s")

start = time.time()
def fibmemo(n):
    memo = {}
    def fib(n):
        if n not in memo:
            if n < 2:
                memo[n]  = n
            else:
                memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    return fib(n)
fibmemo(40)
end = time.time()
mtime = end - start
print("Memo time: " + str("{:.6f}".format(mtime)) + "s")

delta = ntime / mtime
print("Memoization is " + str("{:.2f}".format(abs(delta))) + " times faster than Naive")