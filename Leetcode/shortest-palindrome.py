# https://leetcode.com/problems/shortest-palindrome/

# Given a string s, you can convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
#
# Example 1:
#
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
#
# Input: s = "abcd"
# Output: "dcbabcd"
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only.

# Brute Force approach is very easy. We just need to find the largest palindrome from starting
# and reverse the remaining string and add it to the beginning.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        for i in range(len(s)-1, -1, -1):
            if s[:i+1]==s[:i+1][::-1]:
                return s[i+1:][::-1]+s

# KMP Algorithm

