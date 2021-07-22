"""
11. Container With Most Water

- https://leetcode.com/problems/container-with-most-water/
- Two Pointers, DP

## Challenge

    Given n non-negative integers a1, a2, ..., an , 
    where each represents a point at coordinate (i, ai). 
    
    n vertical lines are drawn such that the two endpoints 
    of the line i is at (i, ai) and (i, 0). 
    
    Find two lines, which, together with the x-axis forms a container, 
    such that the container contains the most water.

    ### Example 1

        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array 
        [1,8,6,2,5,4,8,3,7]. 
        
        In this case, the max area of water the container can contain is 49.

    ### Example 2

        Input: height = [1,1]
        Output: 1

    ### Example 3

        Input: height = [1,2,1]
        Output: 2


    ### Constraints:

        n == height.length
        2 <= n <= 105
        0 <= height[i] <= 104

## Solution

    After being stuck for a long time I looked up at the forums and found this post:

    https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation

    1.  The widest container (using first and last line) is a good candidate, 
        because of its width. 
        Its water level is the height of the smaller one of first and last line.
    2.  All other containers are less wide and thus would need a higher water 
        level in order to hold more water.
    3.  The smaller one of first and last line doesn't support a higher water 
        level and can thus be safely removed from further consideration.

    class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

    From another thread:

        "Bucket theory: how much water a bucket can contain 
        depends on the shortest plank. So, as to find the next 
        potential maximum area, we disregard the shorter end 
        by moving it to the next position."


    ## Personal speed improvements:

    Observation 1. Using a lot of max and min calls while also using height[i] < height[j]
        this can be combined
    Observation 2. The while statement is always doing the same amount of iterations. Use a for loop

    "Runtime: 616 ms, faster than 97.72% of Python3 online submissions for Container With Most Water."

"""
class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        best = curr = 0

        for _ in range(len(height)):

            if height[left] < height[right]:
                curr = (right - left) * height[left]
                left += 1
            else:
                curr = (right - left) * height[right]
                right -= 1

            if best < curr: best = curr

        return best


if __name__ == '__main__':
    print("Running tests.")

    t1 = [1,8,6,2,5,4,8,3,7]
    a1 = 49

    t2 = [1,1]
    a2 = 1

    t3 = [1,2,1]
    a3 = 2

    t4 = [1,2,4,3]
    a4 = 4

    t5 = [1,8,6,2,5,4,8,25,7]
    a5 = 49

    s = Solution()
    f = s.maxArea


    assert f(t1) == a1
    assert f(t2) == a2
    assert f(t3) == a3
    assert f(t4) == a4
    assert f(t5) == a5

    print("All tests passed.")