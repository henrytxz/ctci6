

def binsearch(A, x, l, r):
    while True:
        mid = (l+r)/2
        if l>r or (l==r and x!=A[mid]):
            return None
        if x == A[mid]:
            return mid
        elif x < A[mid]:
            r = mid-1
        else:
            l = mid+1

A = [1,3,4,7,8]
assert binsearch(A, -2, 0, 4) == None
assert binsearch(A, 11, 0, 4) == None
assert binsearch(A, 3, 0, 4) == 1
assert binsearch(A, 8, 0, 4) == 4
