class BTNode(object):
    """
    node of a binary tree
    """
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

def find(root, key):
    if not root:
        return None

    if root.key == key:
        return root
    elif key < root.key:
        return find(root.left, key)
    else:
        return find(root.right, key)

def min_node(root):
    if not root: return None
    while root:
        return min_node(root.left)

def successor(root, key):
    node = find(root, key)
    if not node: return None
    if node.right:
        return min_node(node.right)
    else:
        p = node.parent
        while p:
            if p.left == node:
                return p
            else:
                node = p
                p = node.parent
        return None

def make_tree_for_testing():
    """
            3
           /  \
         1     5
          \   /
          2  4
    """
    three = BTNode(3)
    one = BTNode(1)
    five = BTNode(5)
    two = BTNode(2)
    four = BTNode(4)

    three.left = one
    three.right = five

    one.right = two
    one.parent = three

    five.left = four
    five.parent = three

    two.parent = one

    four.parent = five

    return three

if __name__ == '__main__':
    bst_root = make_tree_for_testing()
    assert not successor(bst_root, 5)
    assert successor(bst_root, 2).key == 3