""" PROBLEM DESCRIPTION
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

""" BINARY SEARCH 

pattern:

while left_pointer <= right_pointer:
    1. calc pivot pointer: (left + right) // 2
    1b. this can lead to overflow in some languages!
    2. check pivot value
    3. if pivot value == target : return found
    4. if pivot value > target: right_pointer = pivot_pointer -1
    5. else: left_pointer = pivot_pointer + 1

Explanation why this end condition works:

Explanation why this end condition works:

1. [1,3,5] target is 4.
2. left_pointer = 0, right_pointer = 2, pivot_pointer = 1
3. pivot value (3) < target (4), set left_pointer to pivot_pointer + 1
4. Array: [5] target is 4
5. left_pointer = 2, right_pointer = 2, pivot_pointer = 2
6. pivot value > target, set right_pointer to pivot_pointer - 1
7. Left_pointer = 2, right_pointer = 1
8. right_pointer < left_pointer : breaks the left_pointer <= right_pointer

1. [1,3,5] target is 2.
2. left_pointer = 0, right_pointer = 2, pivot_pointer = 1
3. pivot value (3) > target (2), set right_pointer to pivot -1
4. left_pointer = 0, right_pointer = 0
5. Array: [1] target is 2
6. pivot < target, set left_pointer to pivot_pointer + 1
7. Left_pointer = 1, right_pointer = 0
8. left_pointer > right_pointer : breaks the left_pointer <= right_pointer
"""

class Solution:

    def search(self, nums: list[int], target: int) -> int:
        """
        After excluding edge cases run a binary search
        """

        # First edge case, it is impossible for the target to exist in the array
        if target < nums[0] or target > nums[-1] : return -1

        # If the search is possible, initialize two pointers 
        # to the start and the end of the array
        left_pointer = 0
        right_pointer = len(nums) -1

        # search loop
        while left_pointer <= right_pointer:

            middle_pointer = (left_pointer + right_pointer) // 2
            middle_value = nums[middle_pointer]

            if middle_value == target: return middle_pointer

            if middle_value < target:
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1

        # no result found
        return -1


n1 = [-1,0,3,5,9,12]
t1 = 9
n2 = [-1,0,3,5,9]
t2 = 2

if __name__ == "__main__":
    s = Solution()
    print(s.search(n1, t1))
    print(s.search(n2, t2))

