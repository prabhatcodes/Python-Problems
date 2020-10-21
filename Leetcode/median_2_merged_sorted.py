# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def arrayVal(nums, idx):
            lenN = len(nums)
            if idx < 0:
                return -math.inf
            if idx >= lenN:
                return math.inf
            return nums[idx]

        len1 = len(nums1)
        len2 = len(nums2)

        if len1 + len2 == 0:
            return 0

        if len1 > len2:
            tmp = nums2
            nums2 = nums1
            nums1 = tmp

            tmp = len1
            len1 = len2
            len2 = tmp

        if (len1 + len2) % 2 == 0:
            midLen = (len1 + len2) // 2
            even = True
        else:
            midLen = (len1 + len2) // 2 + 1
            even = False

        l = -1
        r = len1

        while l <= r:
            midPot1 = l + (r - l) // 2

            midNum1 = arrayVal(nums1, midPot1)

            midPot2 = midLen - (midPot1 + 1) - 1
            midNum2 = arrayVal(nums2, midPot2)

            midNum = max(midNum1, midNum2)

            if midNum > arrayVal(nums1, midPot1 + 1):
                l = midPot1 + 1
                continue
            if midNum > arrayVal(nums2, midPot2 + 1):
                r = midPot1 - 1
                continue
            if even:
                a = arrayVal(nums1, midPot1 + 1)
                b = arrayVal(nums2, midPot2 + 1)
                return (midNum + min(a, b)) * 0.5
            else:
                return midNum

        midPot2 = midLen - (l + 1) - 1
        if midPot2 + 2 >= len(nums2):
            nums2.append(nums1[0])
        else:
            nums2[midPot2 + 2] = min(nums2[midPot2 + 2], nums1[0])
        if even:
            return 0.5 * (nums2[midLen - 1] + nums2[midLen])
        else:
            return nums2[midLen - 1]
