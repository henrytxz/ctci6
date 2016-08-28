def merge_from_A(A, k, i):
    print 'i is {0} and k is {1}'.format(i, k)
    A[k] = A[i]
    A[i] = None
    i-=1
    return i

def merge_from_B(A, B, j, k):
    A[k] = B[j]
    B[j] = None
    j-=1
    return j

def merge(A, B, size_A):
    i = size_A-1
    j = len(B)-1
    k = -1
    while i!=-1 or j!=-1:
        print 'i is {0} and j is {1}'.format(i, j)
        print A
        if i==-1:
            j = merge_from_B(A, B, j, k)
        elif j==-1:
            i == merge_from_A(A, k, i)
        elif A[i] > B[j]:
            i = merge_from_A(A, k, i)
        else:
            j = merge_from_B(A, B, j, k)
        k-=1
    return A[k+1:]

A = [1,3,5,None,None,None]
B = [2,4]
print merge(A, B, size_A=3)