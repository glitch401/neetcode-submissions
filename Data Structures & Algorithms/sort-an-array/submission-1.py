class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    #     if len(nums)<=1:
    #         return nums
        
    #     mid = len(nums)//2
    #     left_sorted = self.sortArray(nums[:mid])
    #     right_sorted = self.sortArray(nums[mid:])

    #     return self.merge(left_sorted, right_sorted)

    # def merge(self, left:List[int], right:List[int])->List[int]:
    #     result = []
    #     i=j=0
    #     while(i<len(left) and j<len(right)):
    #         if left[i]<=right[j]:
    #             result.append(left[i])
    #             i+=1
    #         else:
    #             result.append(right[j])
    #             j+=1

    #     while(i<len(left)):
    #         result.append(left[i])
    #         i+=1
    #     while(j<len(right)):
    #         result.append(right[j])
    #         j+=1
    #     return result
        
        temp = [0]*len(nums)
        
        def merge_sort(l:int, r:int):
            if l>=r:
                return
            mid = (l+r)//2
            merge_sort(l,mid)
            merge_sort(mid+1, r)

            if nums[mid]<=nums[mid+1]:
                return
            
            i, j, k = l, mid+1, l
            while i<=mid and j<=r:
                if nums[i]<=nums[j]:
                    temp[k]=nums[i]
                    i+=1
                else:
                    temp[k]=nums[j]
                    j+=1
                k+=1
            
            while i<=mid:
                temp[k]=nums[i]
                k+=1
                i+=1
            while j<=r:
                temp[k]=nums[j]
                k+=1
                j+=1
            
            nums[l:r+1] = temp[l:r+1]
        
        merge_sort(0, len(nums)-1)
        return nums