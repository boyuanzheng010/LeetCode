# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Store the location
        loc_dict = {}
        # Define the deque to visit
        to_visit = deque([(root, 0)])

        while to_visit:
            node, level = to_visit.popleft()
            loc_dict[level] = node.val
            if node.left:
                to_visit.append((node, level - 1))
            if node.right:
                to_visit.append((node, level + 1))

        result = []
        for loc in sorted(loc_dict.keys()):
            result.append(loc_dict[loc])
        return result