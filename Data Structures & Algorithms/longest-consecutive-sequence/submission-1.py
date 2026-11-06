class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        initial max sequence length
        for loop
        (should i sort it first) 
        check for current + 1 or cuurent - 1
        if present than sequence length + 1
        max_sequence = current_sequence, max_sequence  
        
        '''

        hashset = set(nums)

        max_sequence = 0

        for num in hashset:
            
            if (num-1) not in hashset:

                sequence = 1
                
                while(num+1 in hashset):
                    
                    sequence = sequence + 1

                    num += 1

                max_sequence = max(sequence, max_sequence)

            else: continue

        return max_sequence

