from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            if not node:
                return True

            value = node.val
            if value >= high or value <= low:
                return False

            l = helper(node.left, low, min(high, value))
            r = helper(node.right, max(low, value), high)

            return l and r

        return helper(root, -float('inf'), float('inf'))

