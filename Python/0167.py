class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        ## Challenge:

            Given an array of integers numbers that is already sorted in non-decreasing order, 
            find two numbers such that they add up to a specific target number.

            Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
            where 1 <= answer[0] < answer[1] <= numbers.length.

            The tests are generated such that there is exactly one solution. 
            You may not use the same element twice.

            You can return the answer in any order.

            Example 1:

                Input: numbers = [2,7,11,15], target = 9
                Output: [1,2]
                Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


        ## Solution - Two pointer approach:

            Set a pointer at the start and at the end

            If the sum of those is bigger than the target
            Decrease the last pointer with one step

            If the sum is bigger than the target increase the
            First pointer with one step.   
        """
        pointer_start = 0
        pointer_end = len(nums) - 1

        while nums[pointer_start] + nums[pointer_end] != target:
            if nums[pointer_start] + nums[pointer_end] > target:
                pointer_end -= 1
            else:
                pointer_start += 1

        return [pointer_start  + 1, pointer_end + 1]

if __name__ == "__main__":
    s = Solution()

    res_1 = s.twoSum([2,7,11,15], 9)
    print(res_1)

    res_2 = s.twoSum([2,3,4], 6)
    print(res_2)
