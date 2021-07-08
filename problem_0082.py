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
        

        # Step 1. Find an unique value to start with
        start = None

        # Idea, can we use a previous pointer instead of a counter?
        prev = head
        val = head.val

        while head and not start:
            
            print(f'values processed: {head.val}, start = {start}')

            if val != head.val:
                print(f'{val} is not {head.val}')
                if prev.next != head:
                    print(f'this previous value of {val} was not unique')
                    print('reset the search')
                    prev = head
                    val = head.val
                else:
                    print(f'the previous value {val} seems to have been unique')
                    start = prev

                # edge case, unique value at the end
                if not start and not head.next:
                    print(f'we encounter the first unique value at the end!')
                    start = head

            head = head.next
        
        # Lets see our start value
        return start