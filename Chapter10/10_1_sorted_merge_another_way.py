def merge_from_A(A, i, k):
    A[k] = A[i]
    A[i] = None
    return i-1

def merge(A, B, size_A):
    i = size_A-1
    j = len(B)-1
    k = -1
    while i>= 0:
        if j<0:
            i = merge_from_A(A, i, k)
        elif A[i] >= B[j]:
            i = merge_from_A(A, i, k)
        else:
            A[k] = B[j]
            j-=1
        k-=1
    # print A
    return A[k+1:]


A = [1,3,5,None,None,None,None]
B = [2,4]
assert merge(A, B, size_A=3) == map(lambda x: x+1, range(5))

A = [1,4,None,None,None,None]
B = [2,3]
assert merge(A, B, size_A=2) == [1,2,3,4]

