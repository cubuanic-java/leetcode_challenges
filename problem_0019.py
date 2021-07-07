#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Using 2 pointers with a gap of N

        When the first pointer reaches the end of the array
        Skip the element by connecting the last.next to last.next.next instead
        
        """     
        # set 2 pointers, starting at the head
        first = last = head
        
        # create the gap
        for _ in range(n):
            first = first.next
        
        # Edge case detection: 
        # n equals length of array
        # asked to remove the first element in the array
        # and first is already out of bounds for the while loop
        if first is None:          
            head = head.next
            return head
        
        while first.next:
            last = last.next
            first = first.next
            
        # remove the n-th node by skipping it
        last.next = last.next.next
        
        return head