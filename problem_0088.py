"""
88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/

Classification: Array, Two Pointers
"""


class Solution:
    """
    ## Challenge

        You are given two integer arrays nums1 and nums2, 
        sorted in non-decreasing order, and two integers m and n, 
        representing the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        The final sorted array should not be returned by the function, 
        but instead be stored inside the array nums1. 
        To accommodate this, nums1 has a length of m + n, 
        where the first m elements denote the elements that should be merged, 
        and the last n elements are set to 0 and should be ignored. nums2 has a length of n
    
    ## Solution

        Start at the end with k = m+n-1 and add only the largest values

        If the first while loop runs out then only elements remaining in
        The second array need to be transferred still
        
    """
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m+n-1

        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[k] = nums1[m-1]
                m -= 1
            else:
                nums1[k] = nums2[n-1]
                n -= 1
            k -= 1
        
        while n:
            nums1[k] = nums2[n-1]
            n -= 1
            k -= 1
        

if __name__ == "__main__":
    s = Solution()

    # Example 1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)

    # Example 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    print(nums1)

    # Example 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)    


    