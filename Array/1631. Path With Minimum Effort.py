def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights) #row
        m = len(heights[0]) #cols

        result = [[float("inf")] * m for _ in range(n)]
        result[0][0] = 0

        min_heap = [(0, (0, 0))]
     
        while min_heap:
            diff, (i, j) = heapq.heappop(min_heap)

            if i == n - 1 and j == m - 1:
                return diff

            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
                absdiff = abs(heights[ni][nj] - heights[i][j])
                maxdiff = max(absdiff, diff)

                if result[ni][nj] > maxdiff:
                    result[ni][nj] = maxdiff
                    heapq.heappush(min_heap, (maxdiff, (ni, nj)))

        return result[n - 1][m - 1]