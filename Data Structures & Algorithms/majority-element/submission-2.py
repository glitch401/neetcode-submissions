from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # k,v = count.most_common(1)[0]
        # if v>=len(nums)/2:
        #     return k
        # else: 
        #     return -1
        count, candidate = 0, 0
        for n in nums:
            if count==0:
                candidate=n
            count+=1 if n==candidate else -1
        return candidate