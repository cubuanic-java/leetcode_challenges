class Solution:

    def findMin(self, nums: list[int]) -> int:
        """
        Binary search, but modified end condition

        If the pivot value is bigger than the last value the smallest value has to be at the
        right side of the half.

        Either between the pivot, or the right most value
        Example: [3 4 5 7 1 0 2], 7 > 2 
        Example: [2 3 4 5 7 1 0], 5 > 0

        If the middle value is smaller than the right value: example: [8,9,1,2,3,4,5,6,7]
        The smallest value is on the left side of the pivot, or the pivot itself

        This means we have to modify the usual binary search pattern. 
        Recall binary search:
        while left_pointer <= right_pointer
            check pivot value
            move left to pivot+1 or right to pivot-1 when a match is not found
        
        But because we have no target, we have to keep the right most value in the search.
        Because we keep the right pointer, left and right will never swap like in normal binary search
        They will instead converge to an array of a single value.

        Another explanation can be found here
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation

        The lowest value is found when the pointers converge
        """

        left_pointer = 0
        right_pointer = len(nums) -1

        while left_pointer != right_pointer:
        
            # values in slice
            middle_pointer = (left_pointer + right_pointer) // 2
            middle_value = nums[middle_pointer]
            right_value = nums[right_pointer]

            # update the pointers accordingly
            if middle_value > right_value:
                # there has to be a lower value on the right side of the middle_pointer
                left_pointer = middle_pointer + 1    
            else:
                # recall that the lowest value can be at the middle pointer in this case
                # so we skip the usual -1 from binary search
                right_pointer = middle_pointer

        return nums[left_pointer]


t1 = [1]
t2 = [4,5,6,7,0,1,2]
t3 = [13,15,17,11]
t4 = [4,5,1,2,3]
t5 = [1,2,3,4,5,6]
if __name__ == "__main__":
    s = Solution()

    print(s.findMin(t1))
    print(s.findMin(t2))
    print(s.findMin(t3))
    print(s.findMin(t4))
    print(s.findMin(t5))