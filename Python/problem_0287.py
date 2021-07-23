""" 
# 287. Find the Duplicate Number

- https://leetcode.com/problems/find-the-duplicate-number/
- Classification: Two Pointers, Floyd's Algorithm, Arrays


## Challenge

Given an array of integers nums containing n + 1 integers 
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, 
return this repeated number.

You must solve the problem without modifying 
the array nums and uses only constant extra space.

Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2


## Solution

This problem can be solved using fast and slow pointers
In conjunction with floyd's algorithm

Treat the array as a linked list
- the index is the node head
- the value points to the next node head

index:  0 1 2 3 4
array: [1,3,4,2,2]

[0, 1] > [1, 3] > [3, 2] > [2, 4] > [4, 2] > [2, 4]

Using fast and slow pointers (floyd's algorithm)
Can prove there is a circle in this list

Clear explanation with proof of floyds algorithm:
https://www.youtube.com/watch?v=9YTjXqqJEFE&list=PL3b9zMhRHSShk-kHaXItHwg_c8qn8lnSK&index=3

Explanation how to use it for this particular problem:
https://www.youtube.com/watch?v=dfIqLxAf-8s&list=PL3b9zMhRHSShk-kHaXItHwg_c8qn8lnSK&index=4

Step 1, find the meeting point using fast and slow pointers to prove a loop exist
Step 2, reset one pointer to the start and run them at the same speed till the value's match
"""

class Solution:

    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = 0

        # step 1 detect the loop
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            # NB 1. Finding a meeting point is not finding the value!
            # NB 2. Finding the duplicate value and finding the start of the loop is
            #       Not always the same application of floyds algorithm!
            if slow == fast: break  # Found proof of circle
                

        # Step 2
        # Reset one pointer and move them at 
        # the same speed till the values match
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast: break

        return slow


if __name__ == "__main__":
    s = Solution()

    t1 = [2,5,9,6,9,3,8,9,7,1]
    t2 = [3,1,3,4,2]

    print(s.findDuplicate(t1))
    print(s.findDuplicate(t2))