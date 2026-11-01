class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        word1 = dict()
        word2 = dict()

        for i in s:
            value = word1.get(i,0) + 1
            word1[i] = value

        for i in t:
            value = word2.get(i,0) + 1
            word2[i] = value
        
        return word1 == word2