"""
# 136. Single Number

- https://leetcode.com/problems/single-number/
- Classification: Array, Bit Manipulation


## Challenge

    Given a non-empty array of integers nums, 
    every element appears twice except for one. 
    Find that single one.

    You must implement a solution with a linear runtime 
    complexity and use only constant extra space.


## Solution

1. Naive: 

    Sort the array (n log n)
    Find the missing number

2. Bit Manipulation (XOR)

    https://en.wikipedia.org/wiki/Bitwise_operation#XOR

    - x ^ x = 0
    - x ^ x ^ y = y
"""

class Solution:
    """


    """

    def singleNumber(self, nums: list[int]) -> int:
        """
        Approach 1: sort the array and loop over the array in pairs
        """
        nums = sorted(nums)
        
        for index in range(0, len(nums)-1, 2):
            if nums[index] != nums[index + 1]:
                return nums[index]
        
        # in case it was the last number
        return nums[-1]


    def singleNumber(self, nums: list[int]) -> int:
        """
        XOR Approach
        """
        
        res = 0
        for n in nums:
            res ^= n 
        
        return res
