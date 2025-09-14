def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words_set = set()
        hash_map_word = defaultdict(list)
        hash_map_vowel = defaultdict(list)
        
        for word in wordlist:
            words_set.add(word)
        
        for word in wordlist:
            lower_word = word.lower()
            hash_map_word[lower_word].append(word)
        
        for word in wordlist:
            w_lower = word.lower()
            n_word = ""
            for v in w_lower:
                if v in "aeiou":
                    n_word += "*"
                else:
                    n_word += v
            hash_map_vowel[n_word].append(word)
        

        result = []
        for query in queries:
            q_lower = query.lower()
            n_query = ""
            for v in q_lower:
                if v in "aeiou":
                    n_query += "*"
                else:
                    n_query += v
            if query in words_set:
                result.append(query)
            elif q_lower in hash_map_word:
                result.append(hash_map_word[q_lower][0])
            elif n_query in hash_map_vowel:
                result.append(hash_map_vowel[n_query][0])
            else:
                result.append("")
        
        return (result)