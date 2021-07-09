from collections import deque

class Solution:
    """
    ## Challenge

    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.

    Example 1:
        Input: nums = [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Explanation: After squaring, the array becomes [16,1,0,9,100].
        After sorting, it becomes [0,1,9,16,100].

    Example 2:
        Input: nums = [-7,-3,2,3,11]
        Output: [4,9,9,49,121]
    

    Constraints:

        1 <= nums.length <= 104
        -104 <= nums[i] <= 104
        nums is sorted in non-decreasing order.

    ## Solution

        Pattern: two pointers

        NB! output array still space O(1)

        Step 1. 
            Create an empty output array, with a pointer at the end

                        *
            [_, _, _, _, _]

        Step 2. 
            Pointer at the left and at the right.

             L
            [-7, -3, 2, 3, 11]
                           R
        
        Step 3.
            - Loop over the input array, picking max(L, R)
            - Pre square the values before comparing
            - Move the pointer with the max value to the center
              and calcute the new squared value
            - Decrease the write pointer
    """

    def sortedSquares(self, nums: list[int]) -> list[int]:
        # 1. allocate writing space
        result = [None] * len(nums)

        # 2. Initialize the pointers
        left_pointer = 0
        right_pointer = write_pointer = len(nums)-1

        # For max effeciency, pre-square the values
        # Only the used value needs to be recalculated
        left_squared = nums[left_pointer] ** 2
        right_squared = nums[right_pointer] ** 2
        
        # 3. Two pointers working towards the middle
        while left_pointer <= right_pointer:
            
            if left_squared > right_squared:
                result[write_pointer] = left_squared
                left_pointer += 1
                left_squared = nums[left_pointer] ** 2
            else:
                result[write_pointer] = right_squared
                right_pointer -= 1
                right_squared = nums[right_pointer] ** 2

            write_pointer -= 1

        return result


if __name__ == "__main__":
    s = Solution()

    n1 = [-4,-1,0,3]
    print(n1)
    r1 = s.sortedSquares(n1)
    print(r1)

    n1 = [-7,-3,2,3,11]
    print(n1)
    r1 = s.sortedSquares(n1)
    print(r1)

    n1 = [-6, -5, 0, 3, 4]
    print(n1)
    r1 = s.sortedSquares(n1)
    print(r1)