# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.result = 0

        def dfs(node):
            if not node:
                return
            value = node.val
            if value < low:
                dfs(node.right)
            elif value > high:
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
                self.result += value

        dfs(root)
        return self.result