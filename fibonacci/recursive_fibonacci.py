import time

def recursive_fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return recursive_fibonacci(n-2) + recursive_fibonacci(n-1)

for x in range (1,100):
    t1 = time.time()
    fib = recursive_fibonacci(x)
    t2 = time.time()
    print("fibonacci(%d) = %d (%f seconds)" % (x,fib,t2-t1))