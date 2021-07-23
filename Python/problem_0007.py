class Solution:
    def reverse(self, x: int): # -> int:
        
        sign = 1 if x > 0 else -1 
        reverse_number = 0
        x = abs(x)

        while x != 0:
            # step 1: pop the last digit
            last_digit = x % 10
            x //= 10

            # step 2: push to the result
            reverse_number *= 10 
            reverse_number += last_digit

        if reverse_number > 0x7FFFFFFF:
            return 0

        return sign * reverse_number


if __name__ == "__main__":
    c = Solution()
    t1 = c.reverse(12301)
    print(t1)
    t2 = c.reverse(-123)
    print(t2)
    t2 = c.reverse(0)
    print(t2)
