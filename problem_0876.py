# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    """ 876. Middle of the Linked List

    ## Challenge

        Given a non-empty, singly linked list with head node head, 
        return a middle node of linked list.

        If there are two middle nodes, return the second middle node.


    ## Solution

    Pattern: fast and slow pointers
    
    Step 1.
        Initialize fast and slow pointing at the head
    
    Step 2.
        While fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        Alternative with using try and except:
        The fast = fast.next.next is the first line executed since
        it acts like the check on the while condition
        
        try:
            while True:
                fast = fast.next.next  
                slow = slow.next
        except:
            return slow


        NB: odd: fast.next will be None first
            even: fast will be None first


    Example odd array

    Step 1. Initilizing the pointers:

     #   
    [1, 2, 3, 4, 5]
     *

    Step 2. Move while fast and fast.next

    Iteration 1:
    
           #
    [1, 2, 3, 4, 5]
        *
    
    Iteration 2:
    
                 #
    [1, 2, 3, 4, 5]
           *

        fast.next is None now, iteration will stop.

    
    Even array:

    Step 1. Initialization:

     #
    [1, 2, 3, 4]
     *  


    Step 2. while fast and fast.next

    Iteration 1:
    
           #
    [1, 2, 3, 4]
        *
        
    Iteration 2:
    
                #
    [1, 2, 3, 4]
           *
        
        fast is none now, iteration will stop. 
    """

    # Initial solution
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


    # Try Except solution
    def middleNode(self, head: ListNode) -> ListNode:   
        slow = fast = head
        
        try:
            while True:
                fast = fast.next.next  # This needs to fail first
                slow = slow.next
        except:
            return slow