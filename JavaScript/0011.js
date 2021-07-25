/**
 * @param {number[]} height
 * @return {number}
 */
 var maxArea = function(height) {
    let length = height.length
    let left = 0
    let right = length - 1
    let best = 0
    let curr = 0
    
    for (let i=0; i<length; i++) {
        if (height[left] < height[right]) {
            curr = (right - left) * height[left++]  
        } else {
            curr = (right - left) * height[right--]
        }
        
        if (best < curr) best = curr
    }
    return best
};