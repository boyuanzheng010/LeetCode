# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        # Compare the left and right sub-tree is symmetric in this level
        def compare_left_right(self, left, right):
            # Deal with None situation
            if left == None and right == None:
                return True
            elif left == None and right != None:
                return False
            elif left != None and right == None:
                return False

            # Compare the value
            if left.val != right.val:
                return False

            left_signal = compare_left_right(self, left.left, right.right)
            right_signal = compare_left_right(self, left.right, right.left)

            return left_signal and right_signal

        return compare_left_right(self, root.left, root.right)