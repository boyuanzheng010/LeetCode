# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal_re(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def traversal(root: TreeNode):
            if root == None:
                return None
            output.append(root.val)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return output

    def preorderTraversal_it(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []

        # Push root into the stack
        if root != None:
            stack.append(root)

        # Iterate the stack
        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)

        return output


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def traversal(root: TreeNode):
            if root == None:
                return None
            traversal(root.left)
            output.append(root.val)
            traversal(root.right)

        traversal(root)
        return output


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def traversal(root: TreeNode):
            if root == None:
                return None
            traversal(root.left)
            traversal(root.right)
            output.append(root.val)

        traversal(root)

        return output


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def helper(root, depth):
            if root == None:
                return None

            if len(output) == depth:
                output.append([])

            if root.left != None:
                helper(root.left, depth + 1)
            output[depth].append(root.val)
            if root.right != None:
                helper(root.right, depth + 1)

        helper(root, 0)
        return output






