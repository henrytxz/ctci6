"""
approache this problem as a search problem

1st, notice that 1 rule to obey is parent comes before children in an array

go from the top, root will be 1st element in the array
then 1 node at a time, the collection of arrays each grows by 1,
AND each has a corresponding frontier

   a
  / \
 b   c

going down b => b's children get added to the frontier, and c => different frontier
"""

from copy import copy
from Chapter4.node import Node

def step(A, frontier):
    As = []
    new_fs = []
    for n in frontier:
        B = copy(A)
        B.append(n)
        As.append(B)

        new_frontier = copy(frontier)
        new_frontier.remove(n)
        if n.lc:
            new_frontier.append(n.lc)
        if n.rc:
            new_frontier.append(n.rc)
        new_fs.append(new_frontier)
    return As, new_fs

def bst_to_arrays(bst):
    As = [[]]
    fs = [[bst]]
    As, fs = step(As[0], fs[0])
    # print map(lambda f: f, fs)

    while any(map(lambda f: len(f)>0, fs)):
        newAs = []
        new_fs = []
        for A, f in zip(As, fs):
            newA, new_f = step(A, f)
            newAs.extend(newA)
            new_fs.extend(new_f)
            # As.remove(A)
            # fs.remove(f)
        As = newAs
        fs = new_fs

    print len(As)
    # As = set(As)
    # print len(As)
    for A in As:
        print ','.join(map(lambda node: node.key, A))

if __name__ == '__main__':
    root = Node('2')
    one = Node('1')
    four = Node('4')
    root.lc = one
    root.rc = four
    three = Node('3')
    four.lc = three
    seven = Node('7')
    four.rc = seven
    # root.show()

    bst_to_arrays(root)
