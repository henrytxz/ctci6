import logging
log = logging.getLogger(__name__)

def ms(A, l, r):
    log.info('ms(A,{0},{1})'.format(l,r))
    if l==r:
        return [A[l]]
    L = ms(A, l, (l+r)/2)
    R = ms(A, 1+(l+r)/2, r)
    return merge(L, R)

def merge(A, B):
    C = [None]*(len(A)+len(B))
    i = j = 0
    log.info('A: {0}'.format(A))
    log.info('B: {0}'.format(B))
    for k in range(len(A)+len(B)):
        if i==len(A):
            C[k]=B[j]
            j+=1
        elif j==len(B):
            C[k]=A[i]
            i+=1
        else:
            if A[i]<=B[j]:
                C[k]=A[i]
                i+=1
            else:
                C[k]=B[j]
                j+=1
    return C

A = [3,8,6,1,7,2,8,4]
assert ms(A,0,7) == [1,2,3,4,6,7,8,8]