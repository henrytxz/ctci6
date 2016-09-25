"""
implement get_random_node for a binary tree

idea: in order traversal O(n) algorithm, use the random module to uniformly pick a node

alternatively: store the number of nodes in the left subtree at every node
randomly pick a number <= size of tree
starting from the root, if the rand number is <= size of left subtree, go left,
else, return root (if rand number == size of left subtree + 1) or go right
so when inserting, add 1 to every node on the way
when finding, this doesn't matter at all
when deleting, subtract 1 from all ancestors
"""
from random import choice
from Chapter4.node import Node

class AugmentedNode(Node):
    dummy_key = 'root_parent'

    def __init__(self, key):
        super(AugmentedNode, self).__init__(key)
        self.left_tree_size = 0

    @staticmethod
    def is_root_parent(node):
        return node.key == AugmentedNode.dummy_key

    @staticmethod
    def dummy_node():
        node = AugmentedNode(AugmentedNode.dummy_key)
        return node

class BST(object):
    def __init__(self, root, space_btw_two_bottom_keys=3):
        self.root = AugmentedNode(root)
        self.treesize = 1
        self.space_btw_two_bottom_keys = space_btw_two_bottom_keys

    def draw_grid(self, number_keys_bottom_row):
        grid = []
        children_key_positions = [i*(self.space_btw_two_bottom_keys+1) for i in range(number_keys_bottom_row)]
        grid.insert(0, children_key_positions)
        while len(children_key_positions)>1:
            parents_key_positions = []
            arrow_positions = []
            for i in range(len(children_key_positions)/2):
                parent_key_position = (children_key_positions[2*i]+children_key_positions[2*i+1])/2
                parents_key_positions.append(parent_key_position)
                arrow_positions.append((children_key_positions[2*i]+parent_key_position)/2)
                arrow_positions.append((children_key_positions[2*i+1]+parent_key_position)/2)
            grid.insert(0, arrow_positions)
            grid.insert(0, parents_key_positions)
            children_key_positions = parents_key_positions
        return grid

    def show(self):
        curr_level = [self.root]
        all_levels = [curr_level[:]]
        while curr_level:
            last_level = curr_level[:]
            new_level = []
            for node_above in last_level:
                # node_above = curr_level.pop(0)
                new_level.append(node_above.lc if node_above.lc else AugmentedNode(' '))
                new_level.append(node_above.rc if node_above.rc else AugmentedNode(' '))
            if set([node.key for node in new_level]) == set([' ']):
                break
            all_levels.append(new_level[:])
            curr_level = new_level

        grid = self.draw_grid(len(all_levels[-1]))
        grid_width = grid[-1][-1]+1
        for i, positions in enumerate(grid):
            row = [' '] * grid_width
            if i%2 == 0:
                tree_level = i/2
                for j, p in enumerate(positions):
                    row[p] = str(all_levels[tree_level][j].key)
            else:
                for j, p in enumerate(positions):
                    if j%2 == 0:
                        row[p] = '/'
                    else:
                        row[p] = '\\'
            print ''.join(row)

    def get_random_node(self):
        i = choice(range(self.treesize)) + 1
        curr = self.root
        while True:
            if not curr:
                return None
            if curr.left_tree_size + 1 == i:
                return curr
            elif i <= curr.left_tree_size:
                curr = curr.lc
            else:
                i -= (curr.left_tree_size+1)
                curr = curr.rc

    def insert(self, key):
        self.treesize += 1
        curr = self.root
        while True:
            if key <= curr.key:
                curr.left_tree_size += 1
                if not curr.lc:
                    curr.lc = AugmentedNode(key)
                    return
                else:
                    curr = curr.lc
            else:
                if not curr.rc:
                    curr.rc = AugmentedNode(key)
                    return
                else:
                    curr = curr.rc

    def adjust_size(self, ancestors_to_decrement_left_subtree_size):
        self.treesize -= 1
        for node in ancestors_to_decrement_left_subtree_size:
            node.left_tree_size -= 1

    def delete(self, key):
        # if key is in tree
        # and it's at a leaf, remove it
        # if it has 1 child, connect that node's parent to this child
        # if it has 2 children, get the max from the left subtree and replace the deleted node with it
        found = False
        ancestors_to_decrement_left_subtree_size = []
        curr = self.root
        dummy_direction = 'left'
        while curr:
            parent = None
            if key == curr.key:
                found = True
                if curr == self.root:
                    self.remove_node(curr, (AugmentedNode.dummy_node(), dummy_direction))
                else:
                    self.remove_node(curr, parent)
                break
            elif key < curr.key:
                ancestors_to_decrement_left_subtree_size.append(curr)
                parent = (curr, 'left')
                curr = curr.lc
            else:
                parent = (curr, 'right')
                curr = curr.rc
        if found:
            self.adjust_size(ancestors_to_decrement_left_subtree_size)
        else:
            return  # key not found => nothing to delete

    def remove_helper(self, parent, left_or_right, new_child_node):
        if AugmentedNode.is_root_parent(parent):
            new_child_node.left_tree_size \
                = self.root.left_tree_size -1  # -1 for deleting root
            self.root = new_child_node
        elif left_or_right == 'left':
            parent.lc = new_child_node
        else:
            parent.rc = new_child_node

    def predecessor(self, node):
        # for now, this is predecessor for the case when node has a left subtree
        parent = node
        curr = node.lc
        while curr.rc:
            parent = curr
            curr = curr.rc
        parent.rc = None
        return curr

    def remove_node(self, node, nodes_parent):
        parent, left_or_right = nodes_parent
        if node.lc and node.rc:
            predecessor = self.predecessor(node)
            self.remove_helper(parent, left_or_right, predecessor)
            predecessor.lc = node.lc
            predecessor.rc = node.rc
        elif node.lc:
            self.remove_helper(parent, left_or_right, node.lc)
        elif node.rc:
            self.remove_helper(parent, left_or_right, node.rc)
        else:
            self.remove_helper(parent, left_or_right, None)
        del node


def test_get_random_node(tree, sample_times):
    draws = []
    distinct_keys = set()
    for l in range(4):
        for i in range(sample_times):
            try:
                key_drawn = tree.get_random_node().key
                draws.append(key_drawn)
                distinct_keys.add(key_drawn)
            except Exception:
                print 'oops'

        for element in distinct_keys:
            print '{0} was drawn {1} times'.format(element,
                                                   draws.count(element))
        print '=' * 88
        draws = []

def test_case_1():
    tree = BST(16)
    tree.insert(12)
    tree.insert(18)
    tree.insert(10)
    tree.insert(14)
    tree.insert(20)
    # tree.show()
    test_get_random_node(tree, 600)

def test_case_2():
    tree = BST(3)
    tree.insert(1)
    tree.insert(2)
    tree.insert(5)
    tree.insert(4)
    tree.show()
    print '=' * 28
    tree.delete(3)
    print 'deleted key 3'
    tree.show()
    print '=' * 28
    # for row in tree.draw_grid(4):
    #     print row
    test_get_random_node(tree, 400)

if __name__ == '__main__':
    # test_case_1()
    # print '='*16
    test_case_2()

