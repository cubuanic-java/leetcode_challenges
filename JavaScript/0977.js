/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var sortedSquares = function(nums) {
    let length = nums.length
    let output = new Array(length)
    let left = 0
    let right = length -1
    
    for (let i = right; i >= 0; i--) {
        if (Math.abs(nums[left]) > Math.abs(nums[right])) {
            output[i] = nums[left] * nums[left++]
        } else {
            output[i] = nums[right] * nums[right--] 
        }
    }
    
    return output
};


var sortedSquares = function(nums) {
    return nums.map(x => x * x).sort((a, b) => a - b)
};