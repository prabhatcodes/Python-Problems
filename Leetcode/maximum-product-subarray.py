# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.

# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2,
# because [-2,-1] is not a subarray.

def Solution:
    def maxProduct(self, nums):

        # for empty array

        if not nums:
            return 0

        # there is a need to maintain both previous max & min product
        # as the minimum can be encountered whenever it multiplies
        # by a negative number, but as soon as the negative product
        # is multiplied by a negative number and may give the
        # highest possible number as result

        local_min = local_max = global_max = nums[0]

        for n in nums[1:]:
            temp = local_max # retain the previous local min

            # compute new local max
            # using nums[i] with local max or local min or alone

            local_max = max(n, n*local_max, n*local_min)

            # compute new local min similarly

            local_min = min(n, n*local_min, n*temp)

            global_max = max(global_max, local_max)

        return global_max