# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Follow up: Could you solve it without converting the integer to a string?
#
#
#
# Example 1:
#
# Input: x = 121
# Output: true
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:
#
# Input: x = -101
# Output: false
#
#
# Constraints:
#
# -231 <= x <= 231 - 1

import math


class Solution:
    def get_digit(self, number, n):
        if number - 10 ** n < 0:
            raise ValueError()
        return number // 10 ** n % 10

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True

        digits = int(math.log10(x)) + 1

        i = 0
        while i < digits:
            left = i
            right = digits - 1 - i
            if left >= right: break
            try:
                l = self.get_digit(x, left)
                r = self.get_digit(x, right)
            except ValueError:
                return False
            # print(l,r)
            if l != r:
                return False
            i += 1
        return True