"""
268. Missing Number

- https://leetcode.com/problems/missing-number/
- Classification: Array, Bit Manipulation


## Challenge

    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.


## Solution:

    Using math to calculate the sum of the first consecutive integers:

    sum = 1/2 * n * (n+1)

    https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
"""
class Solution:

    def missingNumber(self, nums: list[int]) -> int:
        length = len(nums)
        math_sum = (length * (length+1)) // 2
        missing = math_sum - sum(nums)
        return missing