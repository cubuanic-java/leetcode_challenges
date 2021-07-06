# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        This is a very fast and slow pointer problem, similar to problem 83

        1.  current node exists and the next node exists check if the value matches 'val'

        2.  same value? skip the node with head.next.next (the fast pointer)
            different value? just move to the next node
            
        3.  Don't forget to store a copy of the head

        4.  Compare this with porblem 0083, we can have an edge case on the start that we need to remove
        """
        
        # keep a copy of the start
        start = head
        
        # remove all the middle and end cases
        while head and head.next:    
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        
        # edge case, matching value on the start
        if start and start.val == val:
            start = start.next
        
        return start