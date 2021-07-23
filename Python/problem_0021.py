"""
# 21. Merge Two Sorted Lists

- https://leetcode.com/problems/merge-two-sorted-lists/
- Classification: Two Pointer


## Challenge

    Merge two sorted linked lists and return it as a sorted list. 
    The list should be made by splicing together the nodes of the first two lists.


## Solution

    Use a new starting head pointing to None

    1. Splice while both lists still hold values into a new head pointer
    2. Add the remaining values
    3. Return start.next
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:      
        start = ListNode(0, None)
        head = start
        
        # Splicing
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1      
                l1 = l1.next        
            else:
                head.next = l2
                l2 = l2.next
            head = head.next        
        
        # Remaininging Values
        if l1: head.next = l1
        if l2: head.next = l2

        return start.next
