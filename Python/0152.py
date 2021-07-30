"""
152. Maximum Product Subarray

- https://leetcode.com/problems/maximum-product-subarray/
- Classification: dynamic programming, array

runtime beats 95.42 % of python3 submissions
"""

class Solution:

    def maxProduct(self, nums: list[int]) -> int:

        def product_pass(nums):
            best_product, curr_product = -float('inf'), 1
            for num in nums:   
                curr_product *= num
                # Reset the value if a zero was encountered
                if not curr_product: curr_product = num
        
                if best_product < curr_product: best_product = curr_product

            return best_product

        forward = product_pass(nums)
        backward = product_pass(nums[::-1])

        if forward > backward:
            return forward
        return backward