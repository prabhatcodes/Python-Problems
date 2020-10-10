# Two Sum
# Given an array of integers, return indices of two numbers
# such that they add up to a specific target.
# We can assume each input to have only one solution.

# Initial Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    return i,j

# Runtime: 6656 ms, faster than 5.00% of Python3 online submissions for Two Sum.
# Memory Usage: 15 MB, less than 15.54% of Python3 online submissions for Two Sum.

# Need to make it faster and consume less memory

# Learning One Pass Method (Using Hashmap ie Dictionary)

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        i = 0
        while i<len(nums):
            if (target - nums[i]) not in seen:
                seen[nums[i]] = i
                i += 1
            else:
                return [seen[target-nums[i]], i]

# Runtime: 40 ms, faster than 98.34% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 15.54% of Python3 online submissions for Two Sum.