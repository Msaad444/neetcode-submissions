class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mp = set()
        l = 0 
        seqlen = 0

        for r in range(len(s)):
            while s[r] in mp:
                mp.remove(s[l])
                l += 1
            mp.add(s[r])

            seqlen = max(r - l + 1 , seqlen)
        
        return seqlen

            
            


        
        
        