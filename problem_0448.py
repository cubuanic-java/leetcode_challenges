class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        See problem 442!

        First pass: mark the numbers visited, just like in p 422.

        Second pass: use list comprehension to return the mising numbers.
        """
        for n in nums:
            n_abs = abs(n)
            if nums[n_abs-1] > 0:
                nums[n_abs-1] *= -1
        
        return [i+1 for i, n in enumerate(nums) if n>0]

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        using a set instead of a mark negative pass, using more space
        """

        nums_set = set(nums)
        missing = []
        for i in range(1, len(nums+1)):
            if i not in nums_set:
                missing.append(i)

        return missing


    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        using a set and list comprehension
        """

        nums_set = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in nums_set]


