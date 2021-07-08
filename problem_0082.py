# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    ## Challenge:

        Given the head of a sorted linked list, 
        delete all nodes that have duplicate numbers, 
        leaving only distinct numbers from the original list. 
        Return the linked list sorted as well.

        Example 1:

            Input: head = [1,2,3,3,4,4,5]
            Output: [1,2,5]
    
        Example 2:
            Input: head = [1,1,1,2,3]
            Output: [2,3]

        
        Constraints:
        >>  The number of nodes in the list is in the range [0, 300].
        >>  -100 <= Node.val <= 100
        >>  The list is guaranteed to be sorted in ascending order.
                
    ## Solution

        Isolate unique elements

    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Edge cases: empty list and single length list
        # No need to perform any searching here
        if not head: return None
        if not head.next: return head
        
        start = ListNode(0, head)
        prev = start
        
        while head:

            # Step 1.   
            # Detect if this is the beginning of a sublist
            # with duplicates that needs to be deleted
            # Or a unique value
            if head.next and head.val == head.next.val:
                # Find the end of this sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skipped all duplicates
                prev.next = head.next
                
            # If this was a unique value move the
            # prev pointer so it gets added to the list
            else:
                prev = prev.next 
                
            # Step 2. 
            # After finding a duplicate list that
            # got deleted, or a unique value that got added
            # move forward in the list
            head = head.next
            
        return start.next