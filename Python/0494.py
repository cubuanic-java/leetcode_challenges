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

    ### Textbook Example 4

        Based on example 4 found in
        'Programming Interview Problems: Dynamic Programming by Leonardo Rossi'
        It utilizes the counter dict.

        But in the book the problem considered is starting at index 1 since the
        First number is not allowed a negative sign.

        partial_result_count = collections.Counter({ numbers[0]: 1 })
        index = 1
        while index < len(nums):
            # logic


    ### Leetcode Forums Clarification

        https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.

        As this resource points out: this is a 0/1 knapsack problem

        0/1 knapsack: take item or not
        Unbounded knapsack: take item as often as you want

        Usual Indicators of a knapsack
        - There is capacity
        - Forced to consider each item
        - There are two states to keep track off: 
            1. current sum 
            2. index (to keep track of what items we have considered)
        - A knapsack usually has two decisions: take or leave

        - Variation: count each value negative or positive
        - Variation: need to fill the space exactly vs optimal (Target vs Capacity)


    ### Final Solution

        1. Start the counter at 1, but the index at zero.

        2. instead of while, use a for loop
            for num in nums

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
    Bottom-up with a defaultdict

    Instead of tabulation DP with an array like in c or java
    A hash map avoids allocating space beforehand
    Slight performance hit for more flexible programming

    Because it is not known if a key exists
    and needs to be updated; or inserted with a fresh value
    a regular dict would throw key errors.
    """
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        from collections import defaultdict

        # Recall: two usual states in a knapsack 0/1 
        # 1: current sum
        #
        # After running BU DP the answer will be in this dict
        # Key: Int, based on adding or substracting the options
        # Val: Number of ways to reach that value
        # Initialize with one possibility 'before' the list
        current_sum = dict({0: 1})  

        # Recall: two usual states in a knapsack 0/1 
        # 2: the index
        # 
        # Equivalent to: nums[idx] for idx in range(len[nums])
        for num in nums:  
            next_sum = defaultdict(int)

            for key, val in current_sum.items():
                next_sum[key + num] += val
                next_sum[key - num] += val
          
            current_sum = next_sum  # No need to keep previous results
        
        return current_sum[target]


if __name__ == '__main__':
    s = Solution()

    r1 = s.findTargetSumWays([1,1,1,1,1], target = 3)
    print(r1)

    r2 = s.findTargetSumWays(nums = [1], target = 1)
    print(r2)
