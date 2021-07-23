""" 
217. Contains Duplicate

- https://leetcode.com/problems/contains-duplicate/
- Classification: Arrays
"""

class Solution:

    def containsDuplicate(self, nums: list[int]) -> bool:
        numbers_seen = set()
        
        for number in nums:
            if number in numbers_seen:
                return True
            else:
                numbers_seen.add(number)
        
        return False