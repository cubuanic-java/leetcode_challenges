"""
# 852. Peak Index in a Mountain Array

- https://leetcode.com/problems/peak-index-in-a-mountain-array/
- Classification: Binary Search

## Challenge:

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, 
return any i such that:
    arr[0] < arr[1] < ... arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1].


Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Example 3:
Input: arr = [0,10,5,2]
Output: 1

Example 4:
Input: arr = [3,4,5,1]
Output: 2

Example 5:
Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2
 

Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.


## Solution

See: 704, 744

Modified binary search where the pivot determines 
if the max value is on the left or the right.


Right Side Mountain Examples

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11]

Left Side Mountain Examples

[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
[11, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

the search will end up at an array of length two if the mountain is on the end

[11, 12], or [12, 11]

the pivot will always point to the first element
compare pivot < pivot + 1 
to check a downhill or still uphill around the pivot
by pushing left and right together we end up with an array of 1, which is the top

while left_pointer != right_pointer

    if pivot < pivot + 1:
        # going uphill, left_pointer to the biggest value
        left_pointer = pivot + 1
    else:
        # going downhill, set right_pointer to the bigger value
        right_pointer = pivot

"""

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left_pointer = 0
        right_pointer = len(arr) - 1

        while left_pointer != right_pointer:
            pivot = (left_pointer + right_pointer) // 2
            
            if arr[pivot] < arr[pivot+1]:
                # going uphill, left_pointer to the biggest value
                left_pointer = pivot + 1
            else:
                # going downhill, set right_pointer to the bigger value
                right_pointer = pivot
            
        return left_pointer


if __name__ == "__main__":
    s = Solution()

    t1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    t2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11]

    print(s.peakIndexInMountainArray(t1))
    print(s.peakIndexInMountainArray(t2))

    t1.reverse()
    t2.reverse()
    print(s.peakIndexInMountainArray(t1))
    print(s.peakIndexInMountainArray(t2))
    
    ex3 = [0,10,5,2] # expected 1
    ex4 = [3,4,5,1] # expected 2
    ex5 = [24,69,100,99,79,78,67,36,26,19] # expected 2

    print(s.peakIndexInMountainArray(ex3))
    print(s.peakIndexInMountainArray(ex4))
    print(s.peakIndexInMountainArray(ex5))