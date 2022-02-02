class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return
        nums.sort()

        result = [
            nums[0] + nums[1] + nums[2],
            [nums[0], nums[1], nums[2]]
        ]

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                cloest = result[0]
                if abs(target - total) < abs(target - cloest):
                    result = [
                        total,
                        [nums[i], nums[l], nums[r]]
                    ]
                if total < target:
                    l += 1
                else:
                    r -= 1

        return result[0]