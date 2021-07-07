# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        This will merge two lists.

        Step 1. Start and head are None at the start.
                Since head will move during a merge process 
                return the starting pointer instead.
        Step 2. Move the head over the lists in increasing values
                This means we need to keep a pointer to the starting point
                to return at the end of the function
        Step 3. Take care of the leftover values from one of the lists
        Step 4. Return the start
        """         
        start = head = None
        
        # Step 1.
        # If both lists exists at the start pick a starting point
        if l1 and l2:
            # print(f'two lists exist, l1: {l1}, l2: {l2}')
            if l1.val < l2.val:
                # print(f'l1 val: {l1.val} and l2 val: {l2.val}, picking l1 as the start')
                start = head = l1
                l1 = l1.next
            else:
                start = head = l2
                l2 = l2.next

        # Step 2.
        # Merge while both lists still hold values    
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1      # assign the value
                l1 = l1.next        # move the list pointer, this might set l1 to None
            else:
                head.next = l2
                l2 = l2.next

            head = head.next        # move the head pointer (one of l1 or l2)
        
        # STEP 3.
        # 2 possible scenarios we are here:
        # - Leftover values after merging 
        # - one list was empty from the start
        if l1:
            if start == None: return l1  # only one list so start was never set
            head.next = l1
        
        if l2:
            if start == None: return l2
            head.next = l2

        # Step 4.
        # if both lists existed a start node was set at the initiliaze part
        # if only one list existed that listNode was returned in Step 3.
        # if no list existed this should be an empty node
        return start
