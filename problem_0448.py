class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        See problem 442!
        """
        for n in nums:
            n_abs = abs(n)
            if nums[n_abs-1] > 0:
                nums[n_abs-1] *= -1
        
        return [i+1 for i in range(0, len(nums)) if nums[i] > 0]