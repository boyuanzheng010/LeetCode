class Solution:
    from collections import deque
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        oldColor = image[sr][sc]
        bias_list = ((-1, 0), (1, 0), (0, 1), (0, -1))

        q = deque()
        q.append((sr, sc))

        while q:
            node = q.popleft()
            x = node[0]
            y = node[1]
            if image[x][y] != oldColor:
                continue
            # visit the current node
            image[x][y] = newColor
            for bias in bias_list:
                r = x + bias[0]
                c = y + bias[1]
                if 0 <= r < len(image) and 0 <= c < len(image[0]):
                    if image[r][c] == oldColor:
                        q.append((r, c))
        return image