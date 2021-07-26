"""
# 70. Climbing Stairs

- https://leetcode.com/problems/climbing-stairs/
- Classification: Dynamic Programming


## Challenge

    You are climbing a staircase. 
    It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?


## Solution 1

    Recursion with memoization
    Using functools lru cache


## Solution 2

    Recurion with memoization
    Using own dict
"""
from functools import lru_cache

class Solution:
    
    # Solution 1
    @lru_cache
    def climbStairs(self, n: int) -> int:
        # if we reach the top we return 1
        if n == 0: return 1
        if n < 0: return 0 # this was illegal 
        
        # not at the top?
        count = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return count


    # Solution 2
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        # if we reach the top we return 1
        if n == 0: return 1
        if n < 0: return 0 # this was illegal 
        
        # not at the top?
        count = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = count
        
        return count