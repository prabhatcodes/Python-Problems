# https://leetcode.com/problems/fraction-to-recurring-decimal/
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# If multiple answers are possible, return any of them.
#
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
#
#
#
# Example 1:
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:
#
# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# Example 4:
#
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"
# Example 5:
#
# Input: numerator = 1, denominator = 5
# Output: "0.2"
#
#
# Constraints:
#
# -231 <= numerator, denominator <= 231 - 1
# denominator != 0

'''
First convert both number into positive integer
Calculate the integer part, put into result list
Then consider the decimal part:
    Using the hashtable to remember each (quotientm, remainder) ->  quotientm's index at result list
    while reminder r != 0:
        calculate q, r = divmod(r*10, denominator)
        if (q, r) exist in hashtable:
            Then we find the repeating sequence, which start from q to the last number in result list
            break the while loop
        else:
            append q into end of list
            cache (q, r) -> len(list) into the hashtable
Lastly, convert the result list into string
'''
import collections


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)

        q, r = divmod(numerator, denominator)
        if not r: return sign + str(q)

        ref = collections.defaultdict(int)
        res = [sign + str(q) + '.']
        ind = len(res)

        while r:
            q, r = divmod(r * 10, denominator)
            if (q, r) not in ref:
                ref[(q, r)] = ind
                res.append(str(q))
                ind += 1
            else:
                re_sInd = ref[(q, r)]
                res[re_sInd] = '(' + res[re_sInd]
                res[-1] = res[-1] + ')'
                break

        return ''.join(res)