class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []

        def backtrace(n: int, k: int, StartIndex: int):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(StartIndex, n + 1):
                path.append(i)
                backtrace(n, k, i + 1)
                path.pop()

        backtrace(n, k, 1)

        return res