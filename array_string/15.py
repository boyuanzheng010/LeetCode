class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This three sum problem could be formulated into a 2sum problem after fixing a number
        def twoSum(subset, target):
            results = set()
            history = {}
            for item in subset:
                if item in history:
                    results.add((item, history[item]))
                else:
                    history[target - item] = item
            return results

        # Iterate each i and perform twoSum on the remaining set
        final_results = set()
        for i in range(len(nums) - 2):
            temp = twoSum(nums[i + 1:], -nums[i])
            if not temp:
                continue
            for item in temp:
                final_results.add(tuple(sorted([item[0], item[1], nums[i]])))
        return map(list, final_results)