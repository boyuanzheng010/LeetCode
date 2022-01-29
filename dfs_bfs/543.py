# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0

        def depth(node, level):
            if not node:
                return level

            l = depth(node.left, level)
            r = depth(node.right, level)
            if l + r > self.diameter:
                self.diameter = (l + r)
            return max(l, r) + 1

        depth(root, 0)
        return self.diameter