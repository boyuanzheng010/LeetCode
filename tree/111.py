# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1

        minimum = 10 ** 9
        if root.left != None:
            minimum = min(self.minDepth(root.left), minimum)
        if root.right != None:
            minimum = min(minimum, self.minDepth(root.right))
        return minimum + 1