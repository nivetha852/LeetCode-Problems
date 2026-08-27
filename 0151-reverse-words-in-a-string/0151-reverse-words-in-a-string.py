class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for ch in s:
            if ch != " ":
                word += ch
            else:
                if word != "":
                    words.append(word)
                    word = ""
                    
        if word != "":
            words.append(word)
            
        result = "" # Initialize the result variable here
        for i in range(len(words) - 1, -1, -1):
            result += words[i]
            if i != 0:
                result += " "
                
        return result