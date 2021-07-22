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
    - See chapter 22 from Rossi

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
        best_chunk = curr_chunk = nums[0]

        for num in nums[1:]:
            if curr_chunk < 0 : curr_chunk = 0
            curr_chunk = curr_chunk + num        
            if best_chunk < curr_chunk: best_chunk = curr_chunk

        return best_chunk



class Solution:
    """
    A call to max is also used a lot on leetcode.
    This works because the next positive value will become the new
    current_chunk when a chunk became negative in the previous run

    But calling max is quite slow.
    """
    def maxSubArray(self, nums: list[int]) -> int:
        best_chunk = prev_chunk = nums[0]
        for num in nums[1:]:
            prev_chunk = max(prev_chunk + num, num)       
            if best_chunk < prev_chunk: best_chunk = prev_chunk

        return best_chunk


class Solution:
    """
    Single pass based on Rossi,
    Seems to throw an error on leetcode
    """
    def maxSubArray(self, nums: list[int]) -> int:
        max_chunk = -float('inf')
        min_chunk = float('inf')
        global_max = -float('inf')

        for value in nums:
            # Compute candidates for the max-product subarray
            # ending with the current element:
            # Candidate 1: Start a new subarray
            max_new_chunk = value
            # Candidate 2: continue positive subarray
            if max_chunk > 0 and value > 0:
                max_continue_positive = max_chunk * value
            else:
                max_continue_positive = -float('inf')
            # Candidate 3: flip sign of negative subarray
            if min_chunk < 0 and value < 0:
                max_flip_negative = min_chunk * value
            else:
                max_flip_negative = -float('inf')
            
            # Compute candidates for the min-product subarray
            # ending with the current element
            # Candidate 1: start a new subarray
            min_new_chunk = value
            # Candidate 2: continue negative subarray
            if min_chunk < 0 and value > 0:
                min_continue_negative = min_chunk * value
            else:
                min_continue_negative = float('inf')
            # Candidate 3: flip sign of positive subarray
            if max_chunk > 0 and value < 0:
                min_flip_positive = max_chunk * value
            else:
                min_flip_positive = float('inf')

            # Choose the best Candidate
            max_chunk = max(max_new_chunk, max_continue_positive, max_flip_negative)
            min_chunk = max(min_new_chunk, min_continue_negative, min_flip_positive)

            # update global max
            if global_max < max_chunk: global_max = max_chunk
    
        return global_max