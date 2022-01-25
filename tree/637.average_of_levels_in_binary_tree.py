# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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

        return [
            sum(item) / len(item) for item in results
        ]