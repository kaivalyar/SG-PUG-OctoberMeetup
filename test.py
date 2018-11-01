from fib import fib
import time

start = time.time()
for i in range(34):
    fib(i)
finish = time.time()
print('calculating took %.3f sec' % (finish-start))
