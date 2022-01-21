class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        expression = set(('+', '-', "*", '/'))

        for item in tokens:
            if item not in expression:
                stack.append(int(item))
            else:
                latter = stack.pop()
                former = stack.pop()
                if item == '+':
                    temp = former + latter
                elif item == '-':
                    temp = former - latter
                elif item == '*':
                    temp = former * latter
                elif item == '/':
                    temp = int(former / latter)
                stack.append(temp)
        return stack[0]