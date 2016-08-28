class Node(object):
    def __init__(self, key):
        self.key = key
        self.lc = None
        self.rc = None

    def print_key(self):
        print '-' * 22
        print '  {0} '.format(self.key)

    def show(self):
        if self.lc and self.rc:
            self.print_key()
            self.show_both_children()
        elif self.lc:
            self.print_key()
            print ' /'
            print '{0}'.format(self.lc.key)
            self.lc.show()
        elif self.rc:
            self.print_key()
            print ' /  \\'
            print '     {0}'.format(self.rc.key)
            self.rc.show()

    def show_both_children(self):
        print ' /  \\'
        print '{0}    {1}'.format(self.lc.key, self.rc.key)
        self.lc.show()
        self.rc.show()

def grow_test_tree():
    root = Node('r')
    root.lc = a = Node('a')
    assert a.key == 'a'
    a.lc = b = Node('b')
    a.rc = g = Node('g')
    g.lc = h = Node('h')
    b.lc = c = Node('c')
    b.rc = d = Node('d')
    c.rc = e = Node('e')
    d.lc = f = Node('f')
    # root.show()
    return root

def is_key_in_tree(root, u):
    # O(height)
    if not root:
        return False
    if root.key == u:
        return True
    else:
        return is_key_in_tree(root.lc, u) or is_key_in_tree(root.rc, u)

def fca(root, u, v):
    u_in_left = is_key_in_tree(root.lc, u)
    v_in_left = is_key_in_tree(root.lc, v)
    if u_in_left and v_in_left:
        return fca(root.lc, u, v)
    elif (u_in_left and not v_in_left) or (not u_in_left and v_in_left):
        return root
    else:
        return fca(root.rc, u, v)

if __name__ == '__main__':
    root = grow_test_tree()
    print 'first common ancestor: node {0}'.format(fca(root, 'e', 'f').key)
