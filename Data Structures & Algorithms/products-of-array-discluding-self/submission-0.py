class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_prod, zero_cnt = 1, 0
        for n in nums:
            if n:
                all_prod *= n
            else:
                zero_cnt+=1
        if zero_cnt>1: return [0]*len(nums)

        output = [0]*len(nums)
        for i,c in enumerate(nums):
            if zero_cnt:
                output[i]=0 if c else all_prod
            else:
                output[i] = all_prod//c
        
        return output
