"""
53. Maximum Subarray

- https://leetcode.com/problems/maximum-subarray/
- classification: sliding window, kadane's algorithm

## Challenge
    
    Given an integer array nums, 
    find the contiguous subarray (containing at least one number) 
    which has the largest sum and return its sum.

## Solution

    - Keep a running sum of all elements add together.
    - Start over when a negative number makes the resulting subarray negative

"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums: return 0

        prev_chunk = -float('inf')
        best_chunk = -float('inf')

        for num in nums:
            if prev_chunk < 0:  # beginning or starting over
                chunk = num
            else:
                chunk = prev_chunk + num

            # update the running maximum
            best_chunk = max(best_chunk, chunk)
            # Record the array chunk
            prev_chunk = chunk

        return best_chunk