class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        
        mid = len(nums)//2
        left_sorted = self.sortArray(nums[:mid])
        right_sorted = self.sortArray(nums[mid:])

        return self.merge(left_sorted, right_sorted)

    def merge(self, left:List[int], right:List[int])->List[int]:
        result = []
        i=j=0
        while(i<len(left) and j<len(right)):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        while(i<len(left)):
            result.append(left[i])
            i+=1
        while(j<len(right)):
            result.append(right[j])
            j+=1
        return result