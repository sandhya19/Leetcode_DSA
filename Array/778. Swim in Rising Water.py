def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid) 

        def can_reach(i, j, t):
            if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] or grid[i][j] > t:
                return False
            
            visited[i][j] = True

            if i == n - 1 and j == n - 1:
                return True
            
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if can_reach(ni, nj, t):
                    return True
            
            return False
        
        l = grid[0][0]
        r = n * n - 1
        result = 0

        while l <= r:
            mid = l + (r - l) // 2
            visited = [[False] * n for _ in range(n)]
            if can_reach(0, 0, mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result
        
        # Dijkstra's
        # n = len(grid) #row
        # m = len(grid[0]) #cols

        # result = [[float("inf")] * m for _ in range(n)]
        # result[0][0] = grid[0][0]

        # min_heap = [(grid[0][0], (0, 0))]
     
        # while min_heap:
        #     t, (i, j) = heapq.heappop(min_heap)

        #     if i == n - 1 and j == m - 1:
        #         return t
            
        #     if t > result[i][j]: continue

        #     for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        #         if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
        #         next_time = max(grid[ni][nj], t)

        #         if result[ni][nj] > next_time:
        #             result[ni][nj] = next_time
        #             heapq.heappush(min_heap, (next_time, (ni, nj)))