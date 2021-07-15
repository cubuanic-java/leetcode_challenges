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

    This is a bottom-up solution using BFS

    Because of the BFS the first path will be the shortest
    It also ignores values that are already in the queue.
    
    For example trying coin 5 and then coin 2 while trying to make 10
    Will skip 2 + 5 since both are 7, and on the same level. 
    This will not take all possible paths into consideration

    'Programming Interview Problems: Dynamic Programming by Leonardo Rossi'

"""
from collections import deque


class Solution:

    def coinChange(self, coins: list[int], amount: int) -> int:
        # Solutions[n] = optimal list of coins that add up to n
        #                None if no solution is known
        solutions = {0: []}

        # Start with zero paid
        ammounts_to_consider = deque([0])

        while ammounts_to_consider:
            paid = ammounts_to_consider.popleft()
            solution = solutions[paid]

            # Due to BFS order the first path is the shortest
            if paid == amount: return len(solution)

            for coin in coins:
                next_paid = paid + coin

                # Skip overshoot payments
                # Note that in the recursive version
                # This was an edge case
                if next_paid > amount: continue

                # Similar ammounts on the same level via
                # different paths are not to be considered   
                if next_paid not in solutions:   
                    solutions[next_paid] = solution + [coin]
                    ammounts_to_consider.append(next_paid)

        return -1  # No combination could reach the result


if __name__ == "__main__":
    s = Solution()

    test_list = [1, 2, 5]
    test_case =  16
    test_result = s.coinChange(test_list, test_case)
    print(test_result)
