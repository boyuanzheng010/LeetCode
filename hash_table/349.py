"""
Basic Solution
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Define dict as hash table
        dict1 = {}
        dict2 = {}

        # Store array into dict
        for item in nums1:
            if item not in dict1:
                dict1[item] = 1
            else:
                dict1[item] += 1

        for item in nums2:
            if item not in dict2:
                dict2[item] = 1
            else:
                dict2[item] += 1

        # Build array using intersection
        intersection = []
        for element in dict1:
            if element in dict2:
                intersection.append(element)
        return intersection
















