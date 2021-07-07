class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        missing = []

        for n in nums:
            if nums[n-1] > 0:
                nums[n-1] *= -1
        
        for i in range(0,len(nums)):
            if nums[i] > 0:
                missing.append(i+1)

        return missing