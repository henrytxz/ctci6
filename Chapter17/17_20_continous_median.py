"""
17.20 continuous median
maintain 2 heaps, a max heap for the bottom half of numbers already seen and a min heap for the top half
idea:
when i see a new number, compare it to max of the max heap, if larger than it, insert into min heap
if less than it, insert into max heap and keep the size of the heaps equal or differ by 1
"""

class MaintainMedian(object):
    def __init__(self):
        self.max_heap = MaxHeap()   # todo: to implement
        self.min_heap = MinHeap()   # todo: to implement

    def insert(self, x):
        if x > self.max_heap.max():
            self.min_heap.insert(x)
        else:
            self.max_heap.insert(x)

        if self.max_heap.size() - self.min_heap.size() > 1:
            element = self.max_heap.extract_max()
            self.min_heap.insert(element)
        elif self.min_heap.size() - self.max_heap.size() > 1:
            element = self.min_heap.extract_min()
            self.max_heap.insert(element)

    def median(self):
        if self.max_heap.size() > self.min_heap.size():
            return self.max_heap.max()
        else:
            return (self.max_heap.max() + self.min_heap.min()) / 2

if __name__ == '__main__':
    mm = MaintainMedian()
    mm.insert(5)
    assert mm.median() == 5
    mm.insert(2)
    assert mm.median() == 3.5
    mm.insert(1)
    assert mm.median() == 2
    mm.insert(8)
    assert mm.median() == 3.5
    mm.insert(3)
    assert mm.median() == 3
