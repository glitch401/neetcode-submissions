class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        # temp = [0]*len(nums)

        # def merge_sort(l,r):
        #     if l>=r:
        #         return
            
        #     mid = (l+r)//2
        #     merge_sort(l,mid)
        #     merge_sort(mid+1, r)

        #     if nums[mid]<=nums[mid+1]:
        #         return

        #     i,j,k = l, mid+1, l
        #     while i<=mid and j<=r:
        #         if nums[i]<=nums[j]:
        #             temp[k]=nums[i]
        #             i+=1
        #         else:
        #             temp[k]=nums[j]
        #             j+=1
        #         k+=1
            
        #     while i<=mid:
        #         temp[k]=nums[i]
        #         i+=1
        #         k+=1
        #     while j<=r:
        #         temp[k]=nums[j]
        #         j+=1
        #         k+=1
        #     nums[l:r+1]=temp[l:r+1]
        
        # merge_sort(0,len(nums)-1)
        # return nums

        count = [0]*3
        for num in nums:
            count[num]+=1
        
        idx = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[idx] = color
                idx+=1
       