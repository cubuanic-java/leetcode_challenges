#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        ## Challenge: To remove the n-th element from the end of the list


        ## Solution: Using the fast and slow pointer pattern.

        - The fast pointer will start with a gap of n away from slow.
        
        - Both pointers will move at the same speed till the fast pointer 
            reaches the end of the list (fast.next is None)
        
        - Skip the nth element by connecting the slow.next to slow.next.next


        ## Example:
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

        Step 4: set #.next (node 3) to #.next.next (node 5)
            return the head of the adjusted list
        

        ## Edge Case: n equals length of list, 
            Solution: skip the first element and return head.next

        Example: l: [1], n = 1

        After step 1 and 2 the pointers will look like:

            # is None: the while loop will throw an exception
        [1]
         *
        """     
        # Step 1: Init fast and slow
        fast = slow = head
        
        # Step 2: Create the gap
        for _ in range(n):
            fast = fast.next
        
        # Step 3: Move fast and slow till fast is at the end
        try:       
            while fast.next:
                slow = slow.next
                fast = fast.next
        except:
            # Edge case: n is list length, skip the first element
            return head.next

        # Step 4. remove the n-th node
        slow.next = slow.next.next
        return head