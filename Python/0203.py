"""
# 203 - Remove Linked List Elements

- https://leetcode.com/problems/remove-linked-list-elements/
- Fast & Slow Pointers


## Challenge

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val,
and return the new head.


## Solution

See also problem 83

1.  current node exists and the next node exists check if the value matches 'val'

2.  same value? skip the node with head.next.next (the fast pointer)
    different value? just move to the next node
    
3.  Don't forget to store a copy of the head

4.  Compare this with porblem 0083, we can have an edge case on the start that we need to remove
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:

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