from Chapter4.node import Node


class RankedNode(Node):
    def __init__(self, key):
        super(RankedNode, self).__init__(key)
        self.index = 0

class RankedTree(object):
    def __init__(self):
        self.root = None
        self.ranks = {}

    def insert(self, curr, new):
        if new.key <= curr.key:
            self.ranks[curr.key][curr.index] += 1
            if curr.lc:
                self.insert(curr.lc, new)
            else:
                self.ranks[new.key][new.index] = self.ranks[curr.key][curr.index]-1 # check
                curr.lc = new
        else:
            if curr.rc:
                self.insert(curr.rc, new)
            else:
                self.ranks[new.key][new.index] = self.ranks[curr.key][curr.index]+1
                curr.rc = new

    def track(self, x):
        n = RankedNode(x)

        if x in self.ranks:
            n.index = len(self.ranks[x])
            self.ranks[x].append(0)
        else:
            self.ranks.setdefault(x, []).append(n.index)

        if self.root:
            self.insert(self.root, n)
        else:
            self.root = n

    def rank(self, x):
        return max(self.ranks[x])

rt = RankedTree()
rt.track(5)
rt.track(1)
rt.track(4)
rt.track(4)
# 1 4 4 5
assert rt.rank(1) == 0
assert rt.rank(4) == 2
assert rt.rank(5) == 3

rt.track(5)
rt.track(9)
rt.track(7)
rt.track(13)
rt.track(3)
# 1 3 4 4 5 5 7 9 13
assert rt.rank(1) == 0
assert rt.rank(3) == 1
assert rt.rank(4) == 3
assert rt.rank(9) == 7
assert rt.rank(13) == 8