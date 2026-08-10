class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            hm[n]=i

        for i,n in enumerate(nums):
            d = target-n
            if d in hm and hm[d]!=i:
                return [i, hm[d]]
        return []