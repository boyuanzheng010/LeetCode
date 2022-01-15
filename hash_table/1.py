class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        history = {}

        for idx, val in enumerate(nums):
            if target - val in history:
                return [history[target - val], idx]
            else:
                history[val] = idx