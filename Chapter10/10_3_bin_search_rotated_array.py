def search_left(A, l, median, r, x):
    if A[l] <= x <= A[median] or \
      (A[l] > A[median] and not (A[median] <= x <= A[r])):
        return True
    else:
        return False

def bin_search(A, l, r, x):
    while l<=r:
        median = (l+r)/2
        if x==A[median]:
            return median
        elif search_left(A, l, median, r, x):
            r = median-1
        else:
            l = median+1
    return -1


if __name__ == '__main__':
    assert bin_search(A=[1, 2, 3, 4, 5], l=0, r=4, x=2) == 1

    assert bin_search(A=[5, 1, 2, 3, 4], l=0, r=4, x=1) == 1

    # print bin_search([4, 5, 1, 2, 3], 0, 4, 5)

    assert bin_search([4, 5, 1, 2, 3], 0, 4, 5) == 1

    assert bin_search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 0, 11, 5) == 8