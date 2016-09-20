"""
t1 and t2 are 2 very large binary trees, t1 much bigger than t2
is t2 a subtree of t1?

worst case to search for a key in a binary tree is O(n), if tree very unbalanced
sps I search for the key of t2's root and find it (if not found, return False)
then from that node in t1, i recursively check left and right subtree to see if t2 is in t1

suppose this breaks down then i look for another occurrence of t2's root
"""

def is_subtree(t2, t1):
    return tree_match(t2, t1) or is_subtree(t2, t1.left) or \
           is_subtree(t2, t1.right)

def tree_match(t2, t1):
    if (t2 and not t1) or (not t2 and t1):
       return False

    return (not t2 and not t1) or \
           ((t1.key == t2.key) and tree_match(t2.left, t1.left) and tree_match(t2.right, t1.right))
