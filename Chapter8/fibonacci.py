# class Fibonacci(object):
#     def __init__(self):
#         self.cache = {}

import time

cache = {}

def fib(n):
    if n==0 or n==1: return n
    if n in cache:
        return cache[n]
    result = fib(n-1)+fib(n-2)
    cache[n] = result
    return result

if __name__ == '__main__':
    # print len([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
    begin = time.time()
    assert map(fib, range(13)) == [0,1,1,2,3,5,8,13,21,34,55,89,144]
    print fib(100)
    print 'done in {0}'.format(time.time()-begin)