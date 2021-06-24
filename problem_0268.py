class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        # Gauss's method forms a general formula for the sum of the first n integers
        # 1/2 * n * (n + 1)
        gaussian_sum = ( length * (length + 1) ) // 2
        
        # now we remove all numbers
        missing = gaussian_sum - sum(nums)
        
        return missing