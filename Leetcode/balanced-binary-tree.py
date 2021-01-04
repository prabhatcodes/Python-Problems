# https://leetcode.com/problems/balanced-binary-tree/

# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:
#
# Input: root = []
# Output: true
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        # Recursive
        def dfs(cur):
            if not cur: return True, 0
            ret_l, ret_r = dfs(cur.left), dfs(cur.right)
            return ret_l[0] and ret_r[0] and (abs(ret_l[1]-ret_r[1])<=1), max(ret_l[1], ret_r[1])+1
        return dfs(root)[0]
        '''
        # Non-recursive
        ret = []
        stack, cur = [], ((root, []), ret)
        while cur[0][0] or stack:
            while cur[0][0]:
                stack.append(cur)
                if cur[0][0].left:
                    cur = ((cur[0][0].left, []), cur[0][1])
                else:
                    cur = ((cur[0][0].right, []), cur[0][1])
            (node, state), p_state = stack.pop()

            ret_l = state[:2] if state else (True, 0)
            ret_r = state[2:] if len(state) > 2 else (True, 0)
            ret_state = (ret_l[0] and ret_r[0] and (abs(ret_l[1] - ret_r[1]) <= 1), max(ret_l[1], ret_r[1]) + 1)
            p_state.extend(ret_state)

            if stack and stack[-1][0][0].left == node:
                cur = ((stack[-1][0][0].right, []), stack[-1][0][1])
            else:
                cur = ((None, None), None)

        return ret[0] if ret else True
