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

            if n==candidate:
                count+=1
            elif n!=candidate and count>0:
                count-=1
            elif count==0:
                candidate=n
                count=1
        return candidate