"""
# 206. Reverse Linked List

- https://leetcode.com/problems/reverse-linked-list/
- Classification: Two Pointers, In place reversal of linked list


## Challenge

Given the head of a singly linked list,
reverse the list, and return the reversed list.


## Solution

To reverse in place is it needed to keep track of
The pointer that a node came from.

1.  At first the previous will be None
    Since the start of the list should become the end and pointing to None

2.  As long as we have a head node we make it point backwards to previous
    But we have to remember what it used to point to so it is possible
    To use that in next iterations

example: (1, 2) -> (2, None)

Iteration 1:
    prev = None
    head = (1, 2)
    next = None

    1. Find out next
    next = (2, None)
    
    2. Make the head point backwards
    head.next = prev (None)
    head = (1, None)

    3.  swap previous with head
        Note: previous becomes the head!
    prev = head (1, None)

    4. Set the head equal to the next node (2)
    head = (2, None)

Iteration 2:
    prev = (1, None)
    head = (2, None)

    1. find out next
    Next = None

    2. Make the head point backwards
    head.next = prev
    head = (2, 1)

    3. swap places with previous
    prev = head = (2, 1)

    4. Make head the next_node
    head = next (None)

This terminates the loop in the next iteration
with the current data structure

prev = (2, 1) -> (1, None)

return prev as this has become the next head
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Working version v1
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        
        while head:
            tmp = head.next         # Store the next node for the loop in tmp
            head.next = reverse     # Reverse in place, head is now pointing back
            reverse = head          # Update the reverse node
            head = tmp              # Move head to next node
        
        return reverse 


    # Version 2
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
   
        while head:
            reverse, reverse.next, head = head, reverse, head.next

        return reverse  
  
