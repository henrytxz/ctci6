"""
t1 and t2 are 2 very large binary trees, t1 much bigger than t2
is t2 a subtree of t1?

worst case to search for a key in a binary tree is O(n), if tree very unbalanced
sps I search for the key of t2's root and find it (if not found, return False)
then from that node in t1, i recursively check left and right subtree to see if t2 is in t1

suppose this breaks down then i look for another occurrence of t2's root
"""
from Chapter4.random_node_4_11 import BST

def is_subtree(t2, t1):
    if not t1 and not t2:
        return True
    if not t1:
        return False
    return tree_match(t2, t1) or is_subtree(t2, t1.lc) or \
           is_subtree(t2, t1.rc)

def tree_match(t2, t1):
    if (t2 and not t1) or (not t2 and t1):
       return False

    return (not t2 and not t1) or \
           ((t1.key == t2.key) and tree_match(t2.lc, t1.lc) and tree_match(t2.rc, t1.rc))

def test_case():
    tree = BST(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(4)
    tree.show()
    print '='*28
    assert is_subtree(None, None)
    assert is_subtree(None, tree.root)  # empty tree is a subtree of tree
    assert is_subtree(tree.root, None) == False # tree not subtree of empty tree

if __name__ == '__main__':
    test_case()