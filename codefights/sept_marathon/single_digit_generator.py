from time import time

def timed_call(f):
    def timed_f(*args):
        begin = time()
        output = f(*args)
        print 'took {0:.3f} seconds'.format(time()-begin, '')
        return output
    return timed_f

@timed_call
def singleDigitGeneratedNumbers(L, R):
    to_mod_by = 10**9+7
    min_length = len(str(L))
    max_length = len(str(R))
    all = []
    for l in xrange(min_length, max_length+1):
        all.extend(gen_for_len(l, L, R))
    return sum(all) % to_mod_by

digits = range(10)
str_digits = [str(x) for x in digits]

def gen_for_len(l, L, R):
    lst = []
    for d in str_digits:
        i = int(d*l)
        if L<=i<=R:
            lst.append(i)
    return lst

assert singleDigitGeneratedNumbers(8, 35) == 83
# print singleDigitGeneratedNumbers(100000000, 600000000)
