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

        Fast and Slow pointer approach.

        Because the initial list gets modified in-place use a dummy head.

        Examples: 
            [] -> []
            [1] -> [1]
            [1, 2] -> [1, 2]
            [1, 1, 2] -> [2]
            [1, 2, 2] -> [1]
        

        slow = start = ListNode(0, head)
        fast = head

        Since the list can start with a duplicate value 
        slow also starts before the array at the same place as start

        Step 1. Determine if there is a duplicate at 
                the start of the search pointer (fast)

                If this is the case:
                - Find the end of this duplicate sublist
                - Remove the sublist by skipping the slow pointer over the sublist
        
        Step 2. After deleting or adding a sublist
                move the fast pointer to the next section in the list

        Not sure if the edge case detection actually makes the code faster

    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Edge cases: empty list and single length list
        # No need to perform any searching here
        if not head: return None
        if not head.next: return head
        
        slow = start = ListNode(0, head)
        fast = head

        while fast:

            # Step 1.   
            # Detect if this is the beginning of a sublist
            # with duplicates that needs to be deleted
            # Or a unique value
            if fast.next and fast.val == fast.next.val:
                # Find the end of this sublist
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                # skipped all duplicates
                slow.next = fast.next
                
            # If this was a unique value move the
            # prev pointer so it gets added to the list
            else:
                slow = slow.next 
                
            # Step 2. 
            # After finding a duplicate list that
            # got deleted, or a unique value that got added
            # move forward in the list
            fast = fast.next
            
        return start.next