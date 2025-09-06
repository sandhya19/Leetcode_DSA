def minOperations(self, queries: List[List[int]]) -> int:
    
    # brute force solution
    # count = 0

    # for i, (l, r) in enumerate(queries):
    #     max_heap = []
    #     for num in range(l, r + 1):
    #         heapq.heappush(max_heap, -num)
    
    #     all_zero = False
    #     while not all_zero:
    #         first_num = -heapq.heappop(max_heap)
    #         second_num = -heapq.heappop(max_heap)
    #         heapq.heappush(max_heap, -(floor(first_num / 4)))
    #         heapq.heappush(max_heap, -(floor(second_num / 4)))
    #         count += 1
    #         all_zero = all(val == 0 for val in max_heap)
    
    # return count

    result = 0
    for i, (l, r) in enumerate(queries):
        # for L and R and S
        # 1 to 3 -- 1 steps
        # 4 to 15 -- 2 steps
        # 16 to 63 -- 3 steps
        L = 1
        S = 1
        steps = 0

        while L <= r:
            R = (4 * L - 1)
            start = max(l, L)
            end = min(r, R)
            
            if start <= end:
                steps += S * (end - start + 1)
            L, S = L * 4, S + 1

        result += int(steps + 1) // 2

    return result