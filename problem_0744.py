"""
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
"""

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str, debug=False) -> str:

        if debug: print(f'input: {letters}, target, {target}')

        # Step 1. Determine the numeric value of the letter given,
        # and the minimum target search value
        ord_target = ord(target) + 1

        if debug: print(f'given target value: {ord_target - 1}, min search value, {ord_target}')
        
        # Step 2. Determine if there is a wrap around, 
        # this happens if the search value is bigger than 
        # the biggest value in the given letter array
        wrap_around = ord_target > ord(letters[-1])

        if debug: print(f'Higest value in letters: {ord(letters[-1])}, wrap around: {wrap_around}')

        if wrap_around:
            return letters[0]

        # Step 3. No wrap around means search for value equal or bigger than target
        left_pointer = 0
        right_pointer = len(letters) - 1

        while left_pointer != right_pointer:

            pivot = (left_pointer + right_pointer) // 2
            ord_pivot = ord(letters[pivot])

            if debug: print(f'''Left index: {left_pointer}, 
                                Pivot index: {pivot}, 
                                Right Index: {right_pointer}''')

            if debug: print(f'''Letter left: {letters[left_pointer]}, 
                                Letter Right: {letters[right_pointer]}''')
            
            # break the loop early if an exact match is found
            if ord_target == ord_pivot:
                return letters[pivot]

            # No exact match found: 
            # Case 1: below the Target, 
            # there has to be better, 
            # Left moves to pivot + 1
            if ord_pivot < ord_target:
                left_pointer = pivot + 1
            # Case 2: above the target, 
            # but it might be the best we can find
            # Right moves to pivot
            if ord_pivot > ord_target:
                right_pointer = pivot
            
            # Edge Case: our best match is above the target 
            # but the letter is multiple times in the array. 
            # That means that left wont move
            # so break when left and right have the same value
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
