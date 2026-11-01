from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)
        val = max(seen.values())
        
        topk = [[] for i in range(val+1)]

        for item,value in seen.items():
            topk[value].append(item)

        res = []
        for i in range(val, 0, -1):
            res.extend(topk[i])
            if len(res) >= k:
                return res[:k]
            




            

            
        