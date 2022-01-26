"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.get_depth(root)

    def get_depth(self, root: 'Node') -> int:
        if root == None:
            return 0
        if root.children == None:
            return 1

        maximun = 0
        for node in root.children:
            temp = self.get_depth(node)
            if temp > maximun:
                maximun = temp
        return maximun + 1