""" Problem 422 - Medium

Given an integer array nums of length n 
where all the integers of nums are in the range [1, n]
and each integer appears once or twice, 
Return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time
and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 
Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.

"""


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """ 
        Due to the constrainst of this problem
        any value-1 can be used as an index pointer.

        This way highest number in the array will never 
        exceed the length of the array index.
        
        Example of a possible array:

        index:  0  1  2  3  4
        array: [1, 2, 3, 4, _] , _ can be 1, 2, 3 or 4

        Solution: loop over the array
            - use the absolute value -1 as an index
            - multiply the value at that index with -1 if it is positive or:
            - if the value at the index is already negative: a double is found

        Alternative:
            - use the absolute value -1 as an index
            - multiply the value at that index with -1
            - if the value at the index is positive that means double negation and a double is found
            - This only works if an alement can not appear 3 or more times
        """
        duplicates = []

        for index in range(len(nums)):

            # grab the absolute value
            value = abs(nums[index])

            # use the value -1 as an index
            # check if the number was altered before 
            # with the negative sign check
            if nums[value -1] > 0:
                nums[value -1] *= -1
            else:
                duplicates.append(value)

        return duplicates

if __name__ == "__main__":
    s = Solution()

    # print(s.findDuplicates([1, 2, 4, 3, 1]))
    print(s.findDuplicates([4,3,2,7,8,3,2,1,5,7]))
