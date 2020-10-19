# Given a string s, find the length of the longest substring
# without repeating characters.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0

def lengthOfLongestSubstring(s):
    dic = {}
    maxi = 0
    temp = 0
    start = 0
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = i
            temp +=1
        else:
            if start>dic[s[i]]:
                temp +=1
                dic[s[i]] = i
            else:
                maxi = max(temp, maxi)
                temp = i-max(start,dic[s[i]])
                start = max(dic[s[i]]+1, start)
                dic[s[i]]=i
    maxi = max(temp,maxi)
    return maxi