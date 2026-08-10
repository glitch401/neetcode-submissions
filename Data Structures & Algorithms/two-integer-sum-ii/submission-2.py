class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_ = len(numbers)-1
        l, r = 0, len_
        while(l<r):
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                l+=1
        return None
            
