"""
322. Coin Change

https://leetcode.com/problems/coin-change/

Patterns: Dynamic Programming, BFS

## Challenge

    You are given an integer array coins representing
    coins of different denominations and an integer 
    amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.

## Solution

    Based on the example found in:
    'Programming Interview Problems: Dynamic Programming by Leonardo Rossi'

    This is a bottom-up solution using BFS

    Because of the BFS the first path will be the shortest
    It also ignores values that are already in the queue.
    
    For example, given coins [1, 2, 5]
    On the second level 5 + 2 is ignored because 2 and 5 are already in the queue


"""
from collections import deque


class Solution:

    """
    This solution stores the path as based on the book
    """
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Store optimal path of coins adding op to a valid amount
        # Initial solution / Edge Case is an empty list
        coin_change_path = {0: []}

        # Build up a BFS queue of coin combinations
        # Start with zero paid (adding a node to tree)
        coin_combinations = deque([0])

        while coin_combinations:
            coin_change = coin_combinations.popleft()

            # BFS: the first path to provide a match
            # Is the shortest path possible
            # For leetcode only return the length
            if coin_change == amount: 
                return len(coin_change_path[amount])

            for coin in coins:
                next_payment = coin_change + coin

                # Skip overshoot payments 
                # End case in recursion
                if next_payment > amount: continue

                # Skip payments already made 
                # via a previous BFS coin change route
                if next_payment in coin_change_path: continue

                # Add the current coin to the 
                # And add this to the queue of payment possibilities
                coin_change_path[next_payment] = coin_change_path[coin_change] + [coin]
                coin_combinations.append(next_payment)

        return -1  # No combination could reach the result

    """
    Storing the depth in the dict instead of the path
    """
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Store Change, Search depth. 
        # Search depth is the number of coins
        # Provide an initial case for zero change
        coin_change_depth = {0: 0}

        # Build up a BFS queue of coin combinations
        # Start with zero paid (adding a node to tree)
        coin_combinations = deque([0])

        while coin_combinations:
            coin_change = coin_combinations.popleft()

            # BFS: the match was reached via the shortest path
            if coin_change == amount: 
                return coin_change_depth[amount]

            for coin in coins:
                next_payment = coin_change + coin

                # Skip overshoot payments 
                # End case in recursion
                if next_payment > amount: continue

                # Skip payments already made 
                # via a previous BFS coin change route
                if next_payment in coin_change_depth: continue

                # Add the current change and depth to the dict
                # And add this to the queue of payment possibilities
                coin_change_depth[next_payment] = coin_change_depth[coin_change] + 1
                coin_combinations.append(next_payment)

        return -1  # No combination could reach the result


if __name__ == "__main__":
    s = Solution()

    test_list = [1, 2, 5]
    test_case =  16
    test_result = s.coinChange(test_list, test_case)
    print(test_result)
