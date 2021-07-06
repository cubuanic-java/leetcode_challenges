# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Floyd's algorithm:
        
        1. Detect if a cycle exists using fast and slow pointers
        2. Move fast and slow till they meet or:
        3. If fast.next is None at some point there is no cycle
           This is detected with the while condition
        4. If a cycle exists reset the slow pointer
           Move slow and fast at the same speed till they meet
        """
        slow = fast = head          # 1. initialize the pointers
        while fast and fast.next:   # See 2 and 3
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:        # 2. Cycle detected!            
                slow = head         # 4. Reset slow and find the start of the cycle
                while slow != fast: 
                    slow = slow.next
                    fast = fast.next                              
                return slow
        
        return None  # While loop found no cycle
        