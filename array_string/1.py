"""
Brute-Force Method
O(n^2)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

"""
Hash-Table
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for i, num in enumerate(nums):
            if num not in history:
                history[target-num] = i
            else:
                return [history[num], i]

