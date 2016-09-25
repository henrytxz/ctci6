"""
65, 100
70, 150
56, 90
75, 190
60, 95
68, 110

key is to handle situations when p1 and p2
p1 is shorter yet heavier

what about sort by ht, then find the longest increasing subseq of wt

1 2 6 7 3 4 5 => correct output 1 2 3 4 5

idea: look at weights, go from left to right
init longest_so_far, abbreviated to lsfar to seq[0]
if new wt > lsfar's last wt, easy
otherwise, backtrack on lsfar till i find a wt < curr wt
=> update longest_ending_at_curr, abbreviated to leacurr
if leacurr has same length as lsfar, replace lsfar (this only happens when curr <= last wt of lsfar so will make future subseqs longer than if we stay with lsfar)
"""

def get_longest_ending_at_curr(seq1, seq2, new_wt):
    j = -1
    while new_wt <= seq1[j]:
        j-=1
    if j < -1:
        seq = seq1[:(j+1)]
    else:
        seq = seq1
    if len(seq1) < len(seq2):
        seq = seq2
    seq.append(new_wt)
    return seq

"""
lsfar   1  2  6 7
leacurr 1  2  6 7
i =     1  2  3 4
seq[i]  2  6  7 3
j =    -1 -2 -3
seq1    1  2  6 7
seq2    1  2
new_wt          3
"""

def longest_subseq(seq):
    if not seq:
        return []
    lsfar = seq[:1]
    leacurr = lsfar
    for i in range(1, len(seq)):
        if seq[i] > lsfar[-1]:
            lsfar.append(seq[i])
            leacurr = lsfar
        else:    # new wt is <= last wt in lsfar
            j = -1
            while seq[i] <= lsfar[j]:
                j-=1
            leacurr = get_longest_ending_at_curr(leacurr, lsfar[:j+1], seq[i])
            if len(leacurr) >= len(lsfar):
                lsfar = leacurr    # curr having <= wt than lsfar will make it at least as long a subseq
    return lsfar

if __name__ == '__main__':
    assert longest_subseq([1,2,6,7,3,4,5]) == [1,2,3,4,5]
    assert longest_subseq([1,2,6,7,4,3,5]) == [1,2,3,5]