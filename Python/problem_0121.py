"""
# Problem 121

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Classification: Dynamic Programming


## Challenge

You are given an array prices where prices[i] 
is the price of a given stock on the ith day.

You want to maximize your profit by choosing 
a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from 
this transaction. 

If you cannot achieve any profit, return 0

Constraints:
- 1 <= prices.length <= 105
- 0 <= prices[i] <= 104


## Solution

The points of interest are the peaks and valleys. 
Find the largest peak following the smallest valley. 
Maintain two variables - minprice and maxprofit corresponding
to the smallest valley and maximum profit 
(maximum difference between selling price and minprice) 
obtained so far respectively.

So any price lower than seen before is greedily set to the
new minimum in the hope a new maximum is found.
"""
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        min_price = 10**4 + 1
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
        