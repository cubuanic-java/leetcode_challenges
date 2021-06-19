"""
Roman to Integer


Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        My approach is to search and remove the special cases first
        Afterwards count the remaining letters normally.

        A different but similar approach would be to seach for the special
        Cases first and replace them with regular roman symbols. 

        Ex: replace IV with IIII
        """

        special_values = {}
        special_values['IV'] = 4
        special_values['IX'] = 9
        special_values['XL'] = 40
        special_values['XC'] = 90
        special_values['CD'] = 400
        special_values['CM'] = 900

        values = {}
        values['I'] = 1
        values['V'] = 5
        values['X'] = 10
        values['L'] = 50
        values['C'] = 100
        values['D'] = 500
        values['M'] = 1000
        
        count = 0
        # count and remove the special values
        for key, val in special_values.items():
            if key in s:
                count += val
                s = s.replace(key, '')

        # count the regular values that are left
        for roman in s:
            count += values[roman]

        return count

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('IV'))
    print(s.romanToInt('MCMXCIV'))
