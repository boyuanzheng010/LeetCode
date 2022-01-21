
class MyStack():

    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop(-1)

    def peek(self):
        return self.items[-1]

    def empty(self):
        return self.items==[]


class Solution:
    def isValid(self, s: str) -> bool:
        # Use the stack to store right side of paraentheses
        stack = MyStack()

        for item in s:
            if item=='(':
                stack.push(')')
            elif item=='[':
                stack.push(']')
            elif item=='{':
                stack.push('}')
            elif stack.empty() or stack.pop( )!=item:
                return False

        return stack.empty()














