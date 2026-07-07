class Solution(object):
    def sumAndMultiply(self, n):
         x = 0
         digit_sum = 0

         for digit in str(n):
             if digit != '0':
                 x = x * 10 + int(digit)
                 digit_sum += int(digit)

         return x * digit_sum
        