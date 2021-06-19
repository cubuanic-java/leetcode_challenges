class Solution:
    def reverse(self, x: int): # -> int:
        
        #if x == 0: return 0
        positive_input = True if x > 0 else False 

        modulo_divisor = 10 if positive_input else -10
        reverse_number = 0

        while True:
            # step 1: select an increasing number of digits with a modulo
            digits_temp = x % modulo_divisor
            # step 2: extract the first digit of the selection with an integer division
            digit = digits_temp // (modulo_divisor // 10)
            # step 3: add the digit to the number
            reverse_number += digit
            # end if the modulo division equals the starting number
            if digits_temp == x: 
                if not positive_input: 
                    reverse_number *= -1
                
                if reverse_number < 2**31 -1 and reverse_number > -2**31:
                    return reverse_number
                else:
                    return 0
            # continue to next 10 fold
            reverse_number *= 10
            modulo_divisor *= 10



if __name__ == "__main__":
    c = Solution()
    t1 = c.reverse(12301)
    print(t1)
    t2 = c.reverse(-123)
    print(t2)
    t2 = c.reverse(0)
    print(t2)
