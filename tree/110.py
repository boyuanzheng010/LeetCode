# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1