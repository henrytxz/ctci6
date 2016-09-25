bst operations (not necessarily balanced)
                                    worst case    average case    best case, suppose n nodes
search                                 O(h)          h/2              1
insert                                 O(h)          h/2              1    (say all nodes are to the left of the root, key > root.key => const time)
delete                                 O(h)          h/2              1    (all but 1 node are to the left of the root, get rid of root.rc)
max                                    O(h)          h/2              1    (say all nodes are to the left of the root)
min                                    O(h)          h/2              1    (say all nodes are to the right of the root)
select (given order statistic)         O(h)          h/2              1    (if I can use extra space, remember the number of nodes in a node's left subtree and the order stats corresponds to the root)
rank                                   O(h)          h/2              1    (if x == root.key and extra space allowed => can just look up left subtree size)
pred                                   O(h)          h/2              1    (a node's lc has no rc and the lc is therefore the max in the left subtree)
succ                                   O(h)          h/2              1    (a node's rc has no lc)

and when not balanced, h is n in the worst case

let's think a bit more about select and rank when extra space isn't allowed
    I can count how many nodes there are in the left subtree
    worst case for count is O(n) per invocation

    suppose n is 100 and order statistic 25
    count(root.lc) returns 50
    if I call count at every move, I may end up calling it O(n) times, each of which is bounded below by 25, i.e. n/2 adding 1s => quadratic
    if I explore more aggressively to a binary-search-like approach: should be O(nlogn), call count logn times, on average each count counts some fraction of n hence nlogn

    rank, worst case will also be quadratic, suppose the tree looks like
    0
     \
      10
     / \
        ..
         \
          80
         / \
           90
          / \
            100
    and rank is implemented as
    def rank(node, key):
        if not node:
            return 0
        if key == node.key:
            return count(node.lc)+1
        elif key < node.key:
            return rank(node.lc, key)
        else:
            return count(node.lc) + 1 + rank(node.rc, key)
    because say key is 95, ~ 10 (n/10) count will get called, each of which maybe n/10 nodes => quadratic
    BUT! I think this way of counting runtime may be flawed, altogether, I may get O(n) because I'm never counting the same thing twice so O(n), I think!
    