/**
 * @param {number[]} nums
 * @return {number}
 */
 var missingNumber = function(nums) {
    // sum of array
    const sum_reducer = (accumulator, currentValue) => accumulator + currentValue;
    const array_sum = nums.reduce(sum_reducer)
    // expected sum = 0.5 * (length * (length+1))
    const length = nums.length
    let consecutive_sum = 0.5 * (length * (length + 1))

    return consecutive_sum - array_sum
};

/**
 * @param {number[]} nums
 * @return {number}
 */
 var missingNumber = function(nums) {
    // expected sum = 0.5 * (length * (length+1))
    const length = nums.length
    let consecutive_sum = 0.5 * (length * (length + 1))

    // remove all numbers present in the array
    for(let i=0; i<length; i++) {
        consecutive_sum -= nums[i]
    }
    
    // only the missing number remains
    return consecutive_sum
};