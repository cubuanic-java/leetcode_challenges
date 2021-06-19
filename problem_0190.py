class Solution:
    def reverse(self, x: int) -> int:

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

    
    def reverseBits(self, n: int) -> int:
        # step 1, calculate the number from the input
        number = 0
        while n != 0:
            
            # step 1: pop the last digit
            last_digit = n % 10
            n //= 10
            
            # step 2: push to the result
            number **= 2 
            number += last_digit

        return number

if __name__ == "__main__":
    c = Solution()
    t1 = c.reverseBits(10100101000001111010011100)
    print(t1)

