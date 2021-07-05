""" Problem 422 - Medium

Given an integer array nums of length n 
where all the integers of nums are in the range [1, n]
 and each integer appears once or twice, 
 eturn an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time 
and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 
Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.

"""

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """ Initial Solution

        start at index 0, check for 1.

        Option 1: the value is correct, n = 1, value is 1, set it to -1
        Option 2: the value is incorrect,
            20, the value is -1, meaning it was swapped here just once!, continue

            2a, swap it with the value at the correct index, mark that index -1
            2a, the value is still not correct. swap again
            2b, the value is correct, set it to -1
            2c, for each swap check if the index is already -1, if it is, add it to doubles

            NB, need to mark a spot as processed.
            ex [4 2 3 5 1]
            The 4 needs to be removed from the array once it goes into the swap queue

        [1 2 4 3 1]

        [-1, 2, 4, 3, 1] index = 0, n = 1 (option 1)
        [-1, -1, 4, 3, 1] index = 1, n = 2 (option 1)
        [-1, -1, 3, -1, 1] index = 2, n = 3 (2a)
        [-1, -1, -1, -1, 1] index = 2, n = 3 (2b)
        [-1, -1, -1, -1, 1] index = 3, n = 4 (20)
        [-1, -1, -1, -1, 0] index = 4, n = 5, 2a, 2c

        duplicates = [1]

        """

        duplicates = {}
        stack = []

        for index in range(len(nums)):

            n_expected = index + 1
            n_actual = nums[index]

            # print(f'Expected value: {expected_val} or -1, actual value: {actual_val}')

            # The value can be incorrect, or swapped here before
            # Only check for duplicates while swapping!

            if n_actual != n_expected and n_actual != -1:
                # mark as being processed!
                nums[index] = -2

                # print(f'putting {actual_val} on the stack')
                stack.append(n_actual)
            else:
                # correct value found
                nums[index] = -1

            while stack:

                val = stack.pop()

                # if this was a duplicate (already -1 ) add it
                # otherwise mark it as -1 for the first time 
                # and check the current value in that spot
                # NB:
                # If we find the correct value 
                # (ex: wanted a 3, found a 3 in the wrong spot, but it is not a duplicate)
                # Mark that spot as -1, otherwise add it to the stack
                if nums[val -1] == -1:
                    duplicates[val] = True
                else:
                    # Store the value currently at the spot for further processing
                    val_ = nums[val -1]

                    # Mark that we swapped the value to the correct spot for the first time
                    nums[val -1] = -1

                    # if currently at the index of the new value, 
                    # so the value at the swap spot matched the expected value at the current index
                    # mark it -1, otherwise add the number to the stack to continue swapping
                    if val_ == n_expected:
                        nums[index] = -1
                    elif val_ != -2: 
                        # -2 was used to indicate this item was processed and no longer of concern
                        # otherwise put it on the stack for another swap
                        # print(f'putting {val_} on the stack from the while loop')
                        stack.append(val_)
                
                # print(nums)

        # return the keys
        return [key for key in sorted(duplicates)]

if __name__ == "__main__":
    s = Solution()

    # print(s.findDuplicates([1, 2, 4, 3, 1]))
    print(s.findDuplicates([4,3,2,7,8,2,3,1,5,7]))
