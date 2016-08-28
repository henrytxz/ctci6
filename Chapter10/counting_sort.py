def counting_sort(A, k):
    L = []
    for j in range(k):
        L.append([])
    for i in range(len(A)):
        L[A[i]].append(A[i])
    output = []
    for j in range(k):
        output.extend(L[j])
    return output

A = [3,8,6,1,7,2,8,4]
assert counting_sort(A, 10) == [1,2,3,4,6,7,8,8]

A = [3,5,7,5,5,3,6]
assert counting_sort(A, 10) == [3,3,5,5,5,6,7]