class Solution:
    from collections import defaultdict, deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prepare the graph and in_degrees
        graph = defaultdict()
        in_degrees = [0] * numCourses
        for target, source in prerequisites:
            in_degrees[target] += 1
            if source not in graph:
                graph[source] = set([target])
            else:
                graph[source].add(target)

        # BFS
        result = []
        q = deque()
        for node, degree in enumerate(in_degrees):
            if degree == 0:
                q.append(node)
        while q:
            node = q.popleft()
            result.append(node)

            if node not in graph:
                continue
            neighbors = graph[node]
            for neighbor in neighbors:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)

        return len(result) == numCourses