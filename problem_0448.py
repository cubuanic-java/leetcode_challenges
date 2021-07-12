"""
# 448. Find All Numbers Disappeared in an Array

- https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
- Classification: Array


## Challenge

Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.


## Solution 1

See problem 442!

First pass: mark the numbers visited, just like in p 422.
Second pass: use list comprehension to return the mising numbers.


## Solution 2

Using a set instead of a mark negative pass, using more space
"""

class Solution:

    # Solution 1
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for n in nums:
            n_abs = abs(n)
            if nums[n_abs-1] > 0:
                nums[n_abs-1] *= -1
        
        return [i+1 for i, n in enumerate(nums) if n>0]


    # Solution 2
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums_set = set(nums)
        missing = []
        
        for i in range(1, len(nums+1)):
            if i not in nums_set:
                missing.append(i)

        return missing


    # Solution 2.1
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums_set = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in nums_set]


