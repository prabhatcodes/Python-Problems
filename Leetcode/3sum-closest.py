# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
# Constraints:
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        res = nums[0] + nums[1] + nums[2]
        mindiff = abs(res - target)

        for i in range(0, n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                temp = nums[i] + nums[left] + nums[right]
                diff = abs(temp - target)

                if temp == target:
                    return temp

                elif temp > target:
                    if diff < mindiff:
                        res = temp
                        mindiff = diff
                    right -= 1

                else:
                    if diff < mindiff:
                        res = temp
                        mindiff = diff
                    left += 1

        return res
