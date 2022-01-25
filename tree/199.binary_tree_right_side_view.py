# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []

        def helper(root, depth):
            if root == None:
                return None
            if len(results) == depth:
                results.append([])
            results[depth].append(root.val)
            if root.left != None:
                helper(root.left, depth + 1)
            if root.right != None:
                helper(root.right, depth + 1)

        helper(root, 0)

        temp = [item[-1] for item in results]

        return temp