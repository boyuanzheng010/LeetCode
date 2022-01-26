class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(path, left, right):
            # Judge the return condition
            if left == right == n:
                res.append(path)

            if left < n:
                backtracking(path + "(", left + 1, right)
            if right < n:
                if left > right:
                    backtracking(path + ")", left, right + 1)

        backtracking("(", 1, 0)
        return res