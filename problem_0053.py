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
    """
    Based on chapter 22 from Rossi
    """
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


class Solution:
    """
    Simplify the negative check and initialize the values at nums[0]
    """
    def maxSubArray(self, nums: list[int]) -> int:
        prev_chunk = best_chunk = nums[0]

        for num in nums[1:]:
            if prev_chunk < 0 : prev_chunk = 0
            prev_chunk = prev_chunk + num     
            if best_chunk < prev_chunk: best_chunk = prev_chunk

        return best_chunk


class Solution:
    """
    A call to max is also used a lot on leetcode.
    This works because the next positive value will become the new
    current_chunk when a chunk became negative in the previous run
    """
    def maxSubArray(self, nums: list[int]) -> int:
        best_chunk = prev_chunk = nums[0]
        for num in nums[1:]:
            prev_chunk = max(prev_chunk + num, num)       
            if best_chunk < prev_chunk: best_chunk = prev_chunk

        return best_chunk


