"""
1. Two Sum

https://leetcode.com/problems/two-sum/


Classification: Arrays
"""

class Solution:
    """
    ## Challenge:

        Given an array of integers nums and an integer target, 
        return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, 
        and you may not use the same element twice.

        You can return the answer in any order.

        Example 1:

            - Input: nums = [2,7,11,15], target = 9
            - Output: [0,1]
            - Output: Because nums[0] + nums[1] == 9, we return [0, 1].
    
    ## Solution:

        Since the input is not guaranteed to be sorted it is not possible
        to use the two pointer approach. See problem 167!

        Loop over the numbers:
            1:  Calculate the compliment number needed to add up to the target
                compliment = target - number

            Two options now:
            2a: The compliment number adding up to the target is already in the dictionary
                Return the result
            2b: Store the number and index in the dictionary if the compliment is not found
    """
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        stored_numbers = {}
        for index, number in enumerate(nums):
            
            compliment = target - number
                       
            if compliment in stored_numbers:
                return [stored_numbers[compliment], index]
            
            stored_numbers[number] = index
            
        # this is an error!
        return -1