# Definition for singly-linked list.
"""
# 234 Palindrome Linked List

- https://leetcode.com/problems/palindrome-linked-list/
- Classification: Fast & Slow pointers


## Challenge:

    Given the head of a singly linked list, 
    return true if it is a palindrome.

    Example 1:
        Input: head = [1,2,2,1]
        Output: true

    Example 2:
        Input: head = [1,2]
        Output: false

    Constraints:
        The number of nodes in the list is in the range [1, 105].
        0 <= Node.val <= 9

   
## Solution:

    Patterns: slow and fast pointers, in-place reversal
    See problem 206 for in place reversal
    See problem 876 to find the middle

    Step 1.
        Initialize fast and slow at the head
        Create a prev node ListNode(0, None)
    
    Step 2.
        While fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            Reverse the list in prev up to slow

    Step 3. 
        Compare the reverse list with the slow list one at a time

        Recall: If the list is odd, fast.next will be None
        Add another step for the slow pointer to skip the odd middle value
        
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: ListNode) -> bool: 
        slow = fast = head
        backwards = None
        
        # Move slow to the middle of the list 
        # Make a backwards copy up till slow
        while fast and fast.next:
            fast = fast.next.next
            backwards, backwards.next, slow = slow, backwards, slow.next

        # In an even list fast will be None
        # We compensate for odd lists
        if fast: slow = slow.next          
            
        # Compare the values
        
        #while slow:
        #    if slow.val != backwards.val: return False
        #    slow = slow.next
        #    backwards = backwards.next
            
        # can also be expressed as
        while slow and slow.val == backwards.val:
            slow = slow.next
            backwards = backwards.next

        return not backwards  # backwards is none if we reach the end of the list