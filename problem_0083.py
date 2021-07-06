# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        This is a very simple fast and slow pointer problem, 

        1.  current node exists and the next node exists check if the value is the same

        2.  same value? skip the node with head.next.next (the fast pointer)
            different value? just move to the next node
            
        3.  Don't forget to store a copy of the head since we change the head

        """
        start = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return start      