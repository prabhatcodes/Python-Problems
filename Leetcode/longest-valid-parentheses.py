# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:
#
# Input: s = ""
# Output: 0
#
#
# Constraints:
#
# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

# Solving using Dynamic Programming https://leetcode.com/problems/longest-valid-parentheses/solution/
# Algorithm
#
# This problem can be solved by using Dynamic Programming. We make use of a \text{dp}dp array where iith element of \text{dp}dp represents the length of the longest valid substring ending at iith index. We initialize the complete \text{dp}dp array with 0's. Now, it's obvious that the valid substrings must end with \text{‘)’}‘)’. This further leads to the conclusion that the substrings ending with \text{‘(’}‘(’ will always contain '0' at their corresponding \text{dp}dp indices. Thus, we update the \text{dp}dp array only when \text{‘)’}‘)’ is encountered.
#
# To fill \text{dp}dp array we will check every two consecutive characters of the string and if
#
# \text{s}[i] = \text{‘)’}s[i]=‘)’ and \text{s}[i - 1] = \text{‘(’}s[i−1]=‘(’, i.e. string looks like ``.......()" \Rightarrow‘‘.......()"⇒
#
# \text{dp}[i]=\text{dp}[i-2]+2dp[i]=dp[i−2]+2
#
# We do so because the ending "()" portion is a valid substring anyhow and leads to an increment of 2 in the length of the just previous valid substring's length.
#
# \text{s}[i] = \text{‘)’}s[i]=‘)’ and \text{s}[i - 1] = \text{‘)’}s[i−1]=‘)’, i.e. string looks like ``.......))" \Rightarrow‘‘.......))"⇒
#
# if \text{s}[i - \text{dp}[i - 1] - 1] = \text{‘(’}s[i−dp[i−1]−1]=‘(’ then
#
# \text{dp}[i]=\text{dp}[i-1]+\text{dp}[i-\text{dp}[i-1]-2]+2dp[i]=dp[i−1]+dp[i−dp[i−1]−2]+2
#
# The reason behind this is that if the 2nd last \text{‘)’}‘)’ was a part of a valid substring (say sub_ssub
# s
# ​
#  ), for the last \text{‘)’}‘)’ to be a part of a larger substring, there must be a corresponding starting \text{‘(’}‘(’ which lies before the valid substring of which the 2nd last \text{‘)’}‘)’ is a part (i.e. before sub_ssub
# s
# ​
#  ). Thus, if the character before sub_ssub
# s
# ​
#   happens to be \text{‘(’}‘(’, we update the \text{dp}[i]dp[i] as an addition of 22 in the length of sub_ssub
# s
# ​
#   which is \text{dp}[i-1]dp[i−1]. To this, we also add the length of the valid substring just before the term "(,sub_s,)" , i.e. \text{dp}[i-\text{dp}[i-1]-2]dp[i−dp[i−1]−2].

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # FIND THE POSTIONS OF THE INVALID OPEN AND CLOSED BRACKETS
        opens = []
        closes = []

        # LOOP THROUGH THE STRING
        for i in range(len(s)):

            # AN OPEN BRACKET - IT COULD BE VALID OR NOT, BUT WE'RE GUARANTEED THAT ALL LEFTOVER BRACKETS IN OPENS WILL BE INVALID AFTER EXITING THE LOOP
            if s[i] == '(':
                opens.append(i)

            # A VALID CLOSED BRACKET
            elif opens:
                opens.pop()

            # AN INVALID CLOSED BRACKET
            else:
                closes.append(i)

        # EDGE CASE : NO INVALID BRACKETS
        if not opens and not closes:
            return len(s)

        # GATHER A SINGLE ARRAY OF OPENED AND CLOSED BRACKET (WRITE A O(N) MERGE HERE)
        merged = sorted(opens + closes)

        # GET THE MAXIMUM DIFF
        return self.max_diff(merged, len(s))

    def max_diff(self, merged, n):
        merged = [-1] + merged + [n]
        diff = 0
        for i in range(1, len(merged)):
            diff = max(diff, merged[i] - merged[i - 1] - 1)
        return diff