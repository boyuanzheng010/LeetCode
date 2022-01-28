from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x, y):
            visited = set()
            queue = deque([(0, 0)])
            steps = 0

            while queue:
                curr_level_cnt = len(queue)
                # iterate through the current level
                for i in range(curr_level_cnt):
                    curr_x, curr_y = queue.popleft()
                    if (curr_x, curr_y) == (x, y):
                        return steps

                    for offset_x, offset_y in offsets:
                        next_x, next_y = curr_x + offset_x, curr_y + offset_y
                        if (next_x, next_y) not in visited:
                            visited.add((next_x, next_y))
                            queue.append((next_x, next_y))

                # move on to the next level
                steps += 1

        return bfs(x, y)


class Solution:
    from collections import deque
    def minKnightMoves(self, x: int, y: int) -> int:
        # Define moves for operation
        moves = ((1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-2, -1), (-1, -2))
        target = set(((x, y), (-x, y), (x, -y), (-x, -y)))
        to_visit = deque([(0, 0, 0)])
        visited = set()

        # Search with BFS algorithm
        while to_visit:
            x_, y_, step = to_visit.popleft()
            if (x_, y_) in target:
                return step
            visited.add((x_, y_))
            for m, n in moves:
                if (x_ + m, y_ + n) not in visited:
                    to_visit.append((x_ + m, y_ + n, step + 1))
                    visited.add((x_ + m, y_ + n))