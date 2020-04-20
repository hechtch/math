import time
import math

PHI = (1+math.sqrt(5))/2

print("PHI: %f" % (PHI))

def const_fibonacci(n):
    return (PHI**n - (1-PHI)**n) / math.sqrt(5)

for x in range (1,100):
    t1 = time.time()
    fib = const_fibonacci(x)
    t2 = time.time()
    print("const_fibonacci(%d) = %d (%f seconds)" % (x,fib,t2-t1))