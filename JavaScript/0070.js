/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    
    let dp_cache = new Array(n+2);
    // base cases
    dp_cache[0] = 0;
    dp_cache[1] = 1;
    
    for(let i = 2; i <= n+1; i++) 
    {
        dp_cache[i] = dp_cache[i-1] + dp_cache[i-2]
    }

    return dp_cache[n+1];
};
