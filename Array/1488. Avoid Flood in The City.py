def avoidFlood(self, rains: List[int]) -> List[int]:
    n = len(rains)
    result = [1] * n
    hash_map = {}
    empty = SortedList()
    
    for i, x in enumerate(rains):
        if x == 0: empty.add(i)
        else: 
            result[i] = -1
            if x in hash_map:
                empty_index = bisect_left(empty, hash_map[x])
                if empty_index == len(empty): return []
                result[empty[empty_index]] = x
                empty.discard(empty[empty_index])
            hash_map[x] = i
            
    return result