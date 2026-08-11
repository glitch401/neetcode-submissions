from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        k,v = count.most_common(1)[0]
        if v>=len(nums)/2:
            return k
        else: 
            return -1