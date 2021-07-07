#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Using 2 pointers with a gap of n

        Move the fast pointer till it reaches the end of the array
        Skip the nth element by connecting the slow.next to slow.next.next

        Example remove n = 3 from the list

        n:  6  5  4  3  2  1
        l: [1, 2, 3, 4, 5, 6]

        Step 1: set fast and slow:

            *
        n:  6  5  4  3  2  1    
        l: [1, 2, 3, 4, 5, 6]
            #

        Step 2: create gap n

                     *
        n:  6  5  4  3  2  1    
        l: [1, 2, 3, 4, 5, 6]
            #        

        Step 3: move both pointers till fast reaches end

                           *
        n:  6  5  4  3  2  1
        l: [1, 2, 3, 4, 5, 6]
                  #           

        Step 4: set #.next to #.next.next
                return head
        
        Edge Case: n equals length of list, skip the first element

        l: [1], n = 1


        Step 3:

        Example: [1], n = 1

            # = None: the while loop will throw an exception
        [1]
         *
            return head.next
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