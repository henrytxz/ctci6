from LinkedList import LinkedList

# def partition(ll, x):
#     """
#     scan the ll, remember prev, if curr < x and it's after x, remove it
#     from the ll and prepend it to the ll
#     """
#     prev = None
#     curr = ll.head
#     after_x = False
#     while curr:
#         if curr.value < x and after_x:
#             prev.next = curr.next
#             curr.next = ll.head
#             ll.head = curr
#             curr = prev.next
#             continue
#         elif curr.value >= x:
#             after_x = True
#             prev = curr
#         curr = curr.next

def partition(linkedlist, x):
    if linkedlist.head != None:
        p1 = linkedlist.head
        p2 = linkedlist.head.next
        while p2 != None:
            if p2.value < x:
                p1.next = p2.next
                p2.next = linkedlist.head
                linkedlist.head = p2
                p2 = p1.next
            else:
                p1 = p1.next
                p2 = p1.next


ll = LinkedList(values=[3,5,8,5,10,2,1])
assert str(ll) == '3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1'
partition(ll, 5)
assert str(ll) == '1 -> 2 -> 3 -> 5 -> 8 -> 5 -> 10'

ll2 = LinkedList(values=[3,6,5,10,2,1])
assert str(ll2) == '3 -> 6 -> 5 -> 10 -> 2 -> 1'
partition(ll2, 5)
assert str(ll2) == '1 -> 2 -> 3 -> 6 -> 5 -> 10'