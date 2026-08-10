class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        numSet = set(numbers)
        for i,n in enumerate(numbers):
            hm[n]=i
        
        for i,n in enumerate(numbers):
            diff = target-n
            if diff in numSet:
                return [i+1, hm[diff]+1]
        return []
