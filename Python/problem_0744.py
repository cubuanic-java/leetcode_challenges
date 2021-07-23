"""
# 744. Find Smallest Letter Greater Than Target

- https://leetcode.com/problems/find-smallest-letter-greater-than-target/ 
- Classification: Binary Search


## Challenge:

Given a characters array letters that is sorted in non-decreasing order 
and a character target, return the smallest character in the array that 
is larger than target. Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 
Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example 3:
Input: letters = ["c","f","j"], target = "d"
Output: "f"

Example 4:
Input: letters = ["c","f","j"], target = "g"
Output: "j"

Example 5:
Input: letters = ["c","f","j"], target = "j"
Output: "c"
 

Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.


## Solution

Binary Search, see 704

Use the ordinal value of the letters.

Step 1. Determine if there is a wrap around.
Step 2. Run a modified binary search:
        The right pointer does not move with a -1 step like in normal binary search
        If left and right have the same value the exact target wont be found
"""

class Solution:

    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        ord_target = ord(target) + 1

        # 1. Detect wrap around
        if ord_target > ord(letters[-1]): return letters[0]

        # 2. Modified Binary Search
        left_pointer = 0
        right_pointer = len(letters) - 1

        while left_pointer != right_pointer:
            pivot = (left_pointer + right_pointer) // 2
            ord_pivot = ord(letters[pivot])

            # Case 1: Exact Match
            if ord_target == ord_pivot: return letters[pivot]

            # Case 2: below the Target 
            # there has to be better at pivot +1
            if ord_pivot < ord_target:
                left_pointer = pivot + 1
            
            # Case 3: above the target, 
            # but it might be the best we can find
            if ord_pivot > ord_target:
                right_pointer = pivot    
            
            # Case 4: our best match is above the target 
            if ord(letters[left_pointer]) == ord(letters[right_pointer]):
                return letters[left_pointer]

        return letters[left_pointer]


if __name__ == "__main__":
    s = Solution()

    ex0 = ['a', 'b']
    ex0_target = 'z'
    ex0_match = 'a'
    print(s.nextGreatestLetter(ex0, ex0_target))

    ex3 = ["c","f","j"]
    ex3_target = "d"
    ex3_match = "f"
    print(s.nextGreatestLetter(ex3, ex3_target))

    ex6 = ["e","e","e","e","e","e","n","n","n","n"]
    ex6_target = "d"
    ex6_match = 'c'
    print(s.nextGreatestLetter(ex6, ex6_target, debug=True))
