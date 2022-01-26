class Solution:
    def __init__(self):
        self.res = []
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.path = ""

    def backtracking(self, digits: str, index: int, k: int):
        if len(self.path) == k:
            self.res.append(self.path[:])
            return
        children = self.letter_map[digits[index]]
        for child in children:
            self.path = self.path + child
            self.backtracking(digits, index + 1, k)
            self.path = self.path[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.backtracking(digits, 0, len(digits))
        return self.res