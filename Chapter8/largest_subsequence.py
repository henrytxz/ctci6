from copy import copy

def largest_subseq(A):
    ls = {}
    ls[-1] = ([0], 0)
    for j in range(len(A)):
        last_seq, last_sum = ls[j-1]
        if last_sum <= 0:
            ls[j] = ([A[j]], A[j])
        else:
            seq = copy(last_seq)
            seq.append(A[j])
            ls[j] = (seq, last_sum+A[j])
    seqs = ls.values()
    return max(seqs, key=lambda (seq, s):s)

A = [5,-1,-3,2,4,3,-1,0]
print largest_subseq(A)

# x = range(3)
# y = copy(x)
# y.append(5)
# print x
# print y