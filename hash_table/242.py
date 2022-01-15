"""
Basic Solution
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Define dict to save string frequency
        s_dict = {}
        t_dict = {}

        for item in s:
            if item in s_dict:
                s_dict[item] += 1
            else:
                s_dict[item] = 1

        for item in t:
            if item in t_dict:
                t_dict[item] += 1
            else:
                t_dict[item] = 1

        return s_dict == t_dict





















