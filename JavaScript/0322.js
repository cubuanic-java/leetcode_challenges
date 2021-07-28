/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
 var coinChange = function(coins, amount) {

    // store change and depth
    // the depth is the number of coins
    // initial case is zero change with zero coins
    let coin_change_depth = {0: 0}
    // BFS Queue
    let bfs_coin_queue = [0]

    while (bfs_coin_queue.length) {
        let coin_change = bfs_coin_queue.shift()

        // Reached amount via bfs, guaranteed least nr coins
        if (coin_change === amount) return coin_change_depth[amount]
        
        for (const coin of coins) {
            let next_payment = coin_change + coin
            
            // skip overshoot
            if (next_payment > amount) continue

            // skip payments already tried (part of BFS)
            if (next_payment in coin_change_depth) continue

            // append the dict and queue
            coin_change_depth[next_payment] = coin_change_depth[coin_change] + 1
            bfs_coin_queue.push(next_payment)
        }
    }
    return -1
};

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
 var coinChange = function(coins, amount) {

    let max = amount+1;
    let dp_cache = new Array(amount+1, max);
    // base case
    dp_cache[0] = 0;
    
    for(let change = 1; change <= amount; change++) 
    {
        let min_coins = max;
        
        for(const coin of coins)
        {
            let prev_change = change - coin;
            
            if(prev_change < 0) continue;
            
            if(dp_cache[prev_change] + 1 < min_coins)
            {
                min_coins = dp_cache[prev_change] +1;
            }            
        }
        dp_cache[change] = min_coins;
    }
    if(dp_cache[amount] === max) return -1;
    return dp_cache[amount];
};