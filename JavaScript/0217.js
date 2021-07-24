/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const numbers_seen = new Set()
    
    for (const num of nums) {
        if (numbers_seen.has(num)){
            return true
        } else {
            numbers_seen.add(num)
        }
    }
    
    return false
};

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const numbers_set = new Set(nums)
    return numbers_set.size !== nums.length
};

