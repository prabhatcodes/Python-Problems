# https://leetcode.com/discuss/explore/fun-with-arrays

# Find maximum consectuive 1s in the array

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = m = 0

        for i in nums:
            if i == 0:
                m = max(m, c)
                c = 0
                continue
            c += 1

        return max(m, c)
