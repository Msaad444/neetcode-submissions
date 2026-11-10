class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dicts = defaultdict(list)

        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if dicts[tmp]:
                return [dicts[tmp], i+1]

            dicts[numbers[i]] = i+1
        return []
       