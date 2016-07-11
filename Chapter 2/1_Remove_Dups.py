from LinkedList import LinkedList

"""
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed
"""

def remove_dups(ll):
    """
    scan the list, add node to seen as you go
    if node seen before, remove it
    """
    seen = set()
    prev = ll.head
    seen.add(prev.value)
    if not prev.next:
        return
    curr = prev.next
    while curr:
        if curr.value in seen:
            prev.next = curr.next
            curr = curr.next
        else:
            seen.add(curr.value)
        prev = prev.next
        if curr:
            curr = curr.next

ll = LinkedList()
ll.add_multiple([2,2,5,3,1,3])
print(ll)
remove_dups(ll)
assert str(ll) == '2 -> 5 -> 3 -> 1'

# ll.generate(100, 0, 9)
# print(ll)
# remove_dups_followup(ll)
# print(ll)
