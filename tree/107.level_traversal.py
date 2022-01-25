# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def helper(root, depth):
            if root == None:
                return None

            if len(output) == depth:
                output.append([])

            output[depth].append(root.val)
            if root.left != None:
                helper(root.left, depth + 1)
            if root.right != None:
                helper(root.right, depth + 1)

        helper(root, 0)

        temp = []
        for i in range(len(output)):
            temp.append(output[len(output) - i - 1])

        return temp