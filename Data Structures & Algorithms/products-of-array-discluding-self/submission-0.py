class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf = [1]*len(nums)
        prod = 1

        for i in range(len(nums)):
            suf[i] = prod
            prod *= nums[i]
            
        
        suff = 1
        for i in range(len(nums)-1,-1,-1):
            suf[i] *= suff
            suff *=  nums[i]
            
        
        return suf        


            
