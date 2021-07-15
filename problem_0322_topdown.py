"""
322. Coin Change

https://leetcode.com/problems/coin-change/

Patterns: Dynamic Programming

## Challenge

    You are given an integer array coins representing
    coins of different denominations and an integer 
    amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.

## Solution

    This is a top-down recursive solution based on:

    'Programming Interview Problems: Dynamic Programming by Leonardo Rossi'

    But even with memoization this is the wrong approach and runs into
    Time Limits Exceeded really quickly
"""

from functools import lru_cache


class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:

        @lru_cache()
        def top_down_recursion(amount):
            # Edge cases
            if not amount: return 0             # done
            if amount < 0: return float('inf')  # punish negative payments
            
            optimal_result = float('inf')

            for coin in coins:
                partial_result = top_down_recursion(amount - coin)
                candidate = partial_result + 1  # used one extra coin
                optimal_result = min(optimal_result, candidate)

            return optimal_result
   
        result = top_down_recursion(amount)
        
        if result == 0: return -1  # indicates payment not possible
        return result


if __name__ == "__main__":
    s = Solution()

    test_list = [1, 2, 5]
    test_case =  16
    test_result = s.coinChange(test_list, test_case)
    print(test_result)
