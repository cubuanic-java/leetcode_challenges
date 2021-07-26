"""
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        open_chars = ['(', '{', '[']
        closing_chars = [')', '}', ']']

        opening_chars = set(open_chars)
        matching_chars = dict(zip(closing_chars, open_chars))

        char_open = []
        
        for char in s:
            # Always accept open chars
            if char in opening_chars: 
                char_open.append(char)
                continue

            # it was a closing char, does it match?
            try:
                if char_open[-1] != matching_chars[char]:
                    #print(f"Error: closing bracket mismatch on {char}")
                    return False
            except IndexError:
                #print("Error: there were no open brackets")
                return False

            # it was a match
            char_open.pop()
        
        # If we have open brackets left return false
        if char_open:
            #print("Error: open chars left")
            return False
        
        # Everything seems okay
        return True

if __name__ == "__main__":
    c = Solution()
    # testcases
    print(c.isValid("()"))
    print(c.isValid("()[]{}"))
    print(c.isValid("(]"))
    print(c.isValid("([)]"))
    print(c.isValid("{[]}"))