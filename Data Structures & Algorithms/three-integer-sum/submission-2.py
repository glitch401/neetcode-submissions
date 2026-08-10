class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums, l = sorted(nums), len(nums)
        for i in range(l):
            if i>0 and nums[i]==nums[i-1]:
                continue
            t = -nums[i]
            j,k = i+1, l-1
            while j<k:
                s = nums[j]+nums[k]
                if s==t:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1

                elif s<t:
                    j+=1
                else:
                    k-=1
        return res



                