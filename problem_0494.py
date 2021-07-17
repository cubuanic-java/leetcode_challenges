"""
494. Target Sum

- https://leetcode.com/problems/target-sum/
- Classification: DP, BFS

## Challenge

    You are given an integer array nums and an integer target.

    You want to build an expression out of nums by adding one 
    of the symbols '+' and '-' before each integer in nums 
    and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2
    and a '-' before 1 and concatenate them to build the expression "+2-1".
    
    Return the number of different expressions that you can build,
    which evaluates to target.

## Solution

    ### Textbook Example 3

        Based on example 3 found in
        'Programming Interview Problems: Dynamic Programming by Leonardo Rossi'
        It utilizes the counter dict.

        But in the book the problem considered is starting at index 1 since the
        First number is not allowed a negative sign.

        partial_result_count = collections.Counter({ numbers[0]: 1 })
        index = 1
        while index < len(nums):
            # logic


    ### Leetcode Clarification

        As this resource points out: this is a knapsack problem

        https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.


    ### Adaptation from book Example

        1. Start the counter at 1, but the index at zero.

        2a. instead of while, use a for loop
            for index in range len(nums):
        2b. for num in nums

        3. Use a default dict instead of a counter
            This gives a huge performance boost

"""
class Solution:
    """
    Top Down Recursive

    Once again top down recursion gives insight into the problem
    But is too slow compared to bottom up because of the function call
    overhead
    """
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        from functools import lru_cache
        """
        Recursive helper function
        """
        target_index = len(nums)
        @lru_cache()
        def recursive_helper(index, partial_result):

            # end condition: index is len nums
            if index == target_index:
                if partial_result == target: return 1
                return 0

            # The recursion, either a plus or a min
            rec_add = recursive_helper(index + 1, partial_result + nums[index])
            rec_sub = recursive_helper(index + 1, partial_result - nums[index])

            return rec_add + rec_sub
        
        # Initialize the recursion
        return recursive_helper(0, 0)

    """
    Bottom-up with Counter from collections
    """
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        from collections import Counter

        # Initialize with one possibility 'before' the list
        partial_result_count = Counter({0: 1})

        # iterate over all the numbers
        for num in nums:
            next_result_count = Counter()

            for prefix_result, count in partial_result_count.items():
                new_add = prefix_result + num
                new_sub = prefix_result - num
                next_result_count[new_add] += count
                next_result_count[new_sub] += count
            
            # replace the dict at each level
            partial_result_count = next_result_count
        
        return partial_result_count[target]

    """
    Bottom-up with a defaultdict

    Reasoning: because it is not known if a key exists
    and needs to be updated; or inserted with a fresh value
    a regular dict will throw key errors.
    """
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        from collections import defaultdict

        # Initialize with one possibility 'before' the list
        partial_result_count = dict({0: 1})

        for num in nums:
            next_result_count = defaultdict(int)

            for prefix_result, count in partial_result_count.items():
                new_add = prefix_result + num
                new_sub = prefix_result - num
                next_result_count[new_add] += count
                next_result_count[new_sub] += count

            # replace the dict at each level            
            partial_result_count = next_result_count
        
        return partial_result_count[target]


if __name__ == '__main__':
    s = Solution()

    r1 = s.findTargetSumWays([1,1,1,1,1], target = 3)
    print(r1)

    r2 = s.findTargetSumWays(nums = [1], target = 1)
    print(r2)
