import time

fib_x_minus_2 = 0
fib_x_minus_1 = 1
for x in range (2,100):
    t1 = time.time()
    fib = fib_x_minus_2 + fib_x_minus_1
    fib_x_minus_2 = fib_x_minus_1
    fib_x_minus_1 = fib
    t2 = time.time()
    print("fibonacci(%d) = %d (%f seconds)" % (x,fib,t2-t1))