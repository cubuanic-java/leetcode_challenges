# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        Floyd's algorithm
        
        A single linked list is like a racetrack
        
        The faster pointer moving twice the speed
        will terminate while the slow pointer is still in the middle
        
        While solving this the order in which we move the pointers is important.
        But why does the try except work in this order for even sized arrays??

        Example odd array

        [1, 2, 3, 4, 5]

        Iteration 1:
        
            #
        [1, 2, 3, 4, 5]
         *
        
        Iteration 2:
        
                  #
        [1, 2, 3, 4, 5]
            *
        
        Iteration 3:
                       #
        [1, 2, 3, 4, 5]
               *
        
        # is None now, next iteration will fail with * in the correct position
        
        Iteration 1:
        
            #
        [1, 2, 3, 4]
         *
         
        Iteration 2:
        
                  #
        [1, 2, 3, 4]
            *
            
        Iteration 3:
        
                    _ # the fast pointer is None before the slow.next line?
        [1, 2, 3, 4]
            * 
        
        Why does the try still execute the slow.next line?
        """
        
        slow = fast = head
        
        try:
            while True:
                fast = fast.next.next
                slow = slow.next
        except:
            return slow
        


    def middleNode(self, head: ListNode) -> ListNode:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow