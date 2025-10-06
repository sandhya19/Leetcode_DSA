def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    n = len(heights)
    m = len(heights[0])

    def bfs(source):
        queue = deque()
        
        if source == 'p':
            for i in range(n): queue.append((i, 0))
            for j in range(m): queue.append((0, j))
        else:
            for i in range(n): queue.append((i, m - 1))
            for j in range(m): queue.append((n - 1, j))
        
        seen = set(queue)

        while queue:
            i, j = queue.popleft()

            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
                if heights[ni][nj] >= heights[i][j] and (ni, nj) not in seen:
                    queue.append((ni, nj))
                    seen.add((ni, nj))
        
        return seen
    
    setp = bfs("p")
    seta = bfs("a")