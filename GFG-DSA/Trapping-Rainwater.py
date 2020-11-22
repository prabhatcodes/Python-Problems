# https://www.geeksforgeeks.org/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
# Examples:
#
# Input: arr[]   = {2, 0, 2}
# Output: 2
# Explanation:
# The structure is like below
#
#
#
# We can trap 2 units of water in the middle gap.
#
# Input: arr[]   = {3, 0, 2, 0, 4}
# Output: 7
# Explanation:
# Structure is like below
# We can trap "3 units" of water between 3 and 2,
# "1 unit" on top of bar 2 and "3 units" between 2
# and 4.  See below diagram also.
#
# Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
#
# Explanation:
# The structure is like below
# Trap "1 unit" between first 1 and 2, "4 units" between
# first 2 and 3 and "1 unit" between second last 1 and last 2

def solution(h):
    water = 0
    leftmax = 0
    rightmax = 0
    l = 0
    r = len(h) - 1
    while l < r:
        if h[l] < h[r]:
            if h[l] >= leftmax:
                leftmax = h[l]
            else:
                water = water + leftmax - h[l]
            l += 1
        else:
            if h[r] >= rightmax:
                rightmax = h[r]
            else:
                water = water + rightmax - h[r]
            r -= 1
    return water

