"""
# 141. Linked List Cycle

- https://leetcode.com/problems/linked-list-cycle/
- Classification: Fast & Slow pointers, Floyd's Algorithm


## Challenge

Given head, the head of a linked list, 
determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node 
in the list that can be reached again by continuously 
following the next pointer. 

Internally, pos is used to denote the index of the node that
tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. 
Otherwise, return false.


## Solution

Floyd's algorithm.

Using fast and slow pointers.

If fast and slow pointers meet there is proof of a loop.
If the fast pointer runs out there is no cicle

This can be implemented with a while fast and fast.next
or a try except
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:

    # Solution 1
    def hasCycle(self, head: ListNode) -> bool:       
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True  # pointers met: a loop detected
        
        return False  # fast pointer reached the end: no loop


    #Solution 1, variant with try except
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head 

        try:
            while True:
                fast = fast.next.next
                slow = slow.next
                if slow == fast: return True
        except:  # .next was None
            return False