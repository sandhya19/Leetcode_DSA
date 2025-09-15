def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split():
            # if any(char in word for char in brokenLetters):
            #     continue
            if set(word) & set(brokenLetters):
                continue
            else:
                count += 1   
            
        return count