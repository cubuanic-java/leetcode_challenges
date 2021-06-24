# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        val_1 = l1.val
        next_1 = l1.next
        val_2 = l2.val
        next_2 = l2.next

        print(val_1, next_1, val_2, next_2)

