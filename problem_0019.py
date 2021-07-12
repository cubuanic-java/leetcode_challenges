"""

- https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- Classification: Fast & Slow Pointers


## Challenge

To remove the n-th element from the end of the list


## Solution: Using the fast and slow pointer pattern.

- The fast pointer will start with a gap of n away from slow.

- Both pointers will move at the same speed till the fast pointer 
    reaches the end of the list (fast.next is None)

- Skip the nth element by connecting the slow.next to slow.next.next


## Example
    remove n = 3 from a list

n:  6  5  4  3  2  1
l: [1, 2, 3, 4, 5, 6]

Step 1: Start fast and slow at the head of the list:

    * (fast)
n:  6  5  4  3  2  1    
l: [1, 2, 3, 4, 5, 6]
    # (slow)

Step 2: create gap n

                *
n:  6  5  4  3  2  1    
l: [1, 2, 3, 4, 5, 6]
    #        

Step 3: move both pointers till fast reaches end
    (while fast.next: move pointers)
    the slow pointer is now at n-1

                    *
n:  6  5  4  3  2  1
l: [1, 2, 3, 4, 5, 6]
          #           

Step 4: skip #.next (node 3 from the end)
    return the head of the adjusted list


## Edge Case: n equals length of list, 
    Solution: skip the first element and return head.next

Example: l: [1], n = 1

After step 1 and 2 the pointers will look like:

    # is None: the while loop will throw an exception
[1]
    *

"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        
        for _ in range(n):  # Create the gap
            fast = fast.next
        
        try:       
            while fast.next:  # Move till end
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next  # Remove the n-th node
            return head
        except:
            return head.next  # n is list length, skip the first element
