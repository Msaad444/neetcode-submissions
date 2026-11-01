class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anag = {}

        for word in strs:
            l_chars = "".join(sorted(word))

            if l_chars in anag:
                anag[l_chars].append(word)
            else:    
                anag[l_chars] = [word]
        
        return list(anag.values())
        