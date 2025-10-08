def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(potions)
        potions.sort()
        result = []

        @cache
        def binary_search(spell):
            l, r = 0, m - 1
            while l <= r:
                mid = l + (r - l) // 2
                if spell * potions[mid] >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            return l


        for spell in spells:
            l = binary_search(spell)
            result.append(m - l) 
        
        return result