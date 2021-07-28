class Solution {
public:
    int coinChange(vector<int>& coins, int amount) 
    {
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        
        // create a cache for the bottom up approach.
        // Zero indexed, and the base case is zero
        // So the length of the cache is amount + 1
        int Max = INT_MAX-1;
        vector<int> dp_cache(amount + 1, Max);
        
        // set the base case
        dp_cache[0] = 0;
        
        // the base case is zero, so we start all next cases at 1
        // till we reach the desired amount
        for(int change=1; change <= amount; change++)
        {
            int min_coins = Max;
            
            for(int coin : coins)
            {
                // going bottom up by trying to find pre calculated values
                int next_change = change - coin;
                
                // skip negative payments
                if (next_change < 0) continue;
                
                // update the minimum count when applicable
                if (dp_cache[next_change] + 1 < min_coins)
                {
                    min_coins = dp_cache[next_change] + 1;
                }
            }
            
            // store the bottom-up result
            dp_cache[change] = min_coins;            
        }
        
        // return the result. if the result is still INT_MAX we did not solve the problem and return -1
        if(dp_cache[amount] == Max) return -1;
        
        return dp_cache[amount];
    }
};

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) 
    {
        ios::sync_with_stdio(false);
        cin.tie(NULL);
        
        // create a cache for the bottom up approach.
        // Zero indexed, and the base case is zero
        // So the length of the cache is amount + 1
        vector<int> dp_cache(amount + 1, INT_MAX-1);
        
        // set the base case
        dp_cache[0] = 0;
        
        // the base case is zero, so we start all next cases at 1
        // till we reach the desired amount
        for(int change=1; change <= amount; change++)
        {           
            for(int coin : coins)
            {
                // going bottom up by trying to find pre calculated values
                int prev_change = change - coin;
                
                // skip negative payments
                if (prev_change < 0) continue;
                
                // update the minimum count when applicable
                if (dp_cache[prev_change] + 1 < dp_cache[change])
                {
                    dp_cache[change] = dp_cache[prev_change] + 1;
                }
            }        
        }
        
        // return the result. if the result is still INT_MAX we did not solve the problem and return -1
        if(dp_cache[amount] == INT_MAX-1) return -1;
        
        return dp_cache[amount];
    }
};
