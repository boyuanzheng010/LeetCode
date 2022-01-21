class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for item in s:
            if stack == []:
                stack.append(item)
            elif item == stack[-1]:
                stack.pop()
            else:
                stack.append(item)

        return ''.join(stack)