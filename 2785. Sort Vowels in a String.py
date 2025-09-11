def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        array = []
        hash_map = defaultdict(int)
        for char in s:
            if char in vowels:
                hash_map[char] += 1
        
        str_list = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                while hash_map[vowels[j]] == 0:
                    j += 1
                str_list[i] = vowels[j]
                hash_map[vowels[j]] -= 1
                
        return ''.join(str_list)
    