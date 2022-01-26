class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Global variables to record paths and final result
        path = []
        res = []

        def backtracking(candidates, target, summ, start):
            if summ == target:
                res.append(path[:])
            if summ >= target:
                return

            for i in range(start, len(candidates)):
                element = candidates[i]
                summ += element
                path.append(element)
                backtracking(candidates, target, summ, i)
                summ -= element
                path.pop()

        backtracking(candidates, target, 0, 0)
        return res