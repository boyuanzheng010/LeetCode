class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Remove pruncation
        for item in "!?',;.":
            paragraph = paragraph.replace(item, " ")
        # Count word frequency
        freq = {}
        banned = set(banned)
        for word in paragraph.lower().strip().split(' '):
            if (word=='') or (word in banned):
                continue
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        # Return the most frequent word
        index = -1
        maxi = -1
        for item in freq:
            if freq[item]>maxi:
                index = item
                maxi = freq[item]
        return index