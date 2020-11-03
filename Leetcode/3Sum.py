# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sorting the array to make the pointer movement choice obvious
        nums.sort()

        # Final result goes here
        res = []

        # Go through each element as a candidate
        for i in range(len(nums)):

            # Skip away the repeats, prevent duplicates
            if i != 0 and nums[i] == nums[i - 1]: continue

            # Reducing question to 2Sum
            target = -nums[i]

            # Basic 2 pointer approach to find all the elemnts possible
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:

                    # You found 1, add it
                    res.append((nums[i], nums[l], nums[r]))

                    # Skip ahead of the same guys both sides
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1

                    # Mandatory obvious movement
                    l += 1
                    r -= 1

                # Selective movements

                # We are behind the target, need a greater number than the current l
                elif nums[l] + nums[r] < target:
                    l += 1

                # We have jumped ahead, choose a smaller number for r
                else:
                    r -= 1
        return res
