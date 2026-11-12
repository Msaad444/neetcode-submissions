class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        MaxA = 0

        while(i<j):
            Area = min(heights[i], heights[j]) * ((j+1)-(i+1))

            if(heights[i] > heights[j]):
                j-=1 
            
            else:
                i+=1
            
            MaxA = max(MaxA, Area)

        return MaxA
