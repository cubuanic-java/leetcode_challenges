/**
 * @param {number} n
 * @return {number}
 */
 var climbStairs = function(n) {
    
    let dp_cache = new Array(n+1);
    // base cases
    dp_cache[0] = 1;
    dp_cache[1] = 2;
    
    for(let i = 2; i < n; i++) 
    {
        dp_cache[i] = dp_cache[i-1] + dp_cache[i-2]
    }

    return dp_cache[n];
};
