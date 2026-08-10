class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a, n = 0, len(heights)
        l, r = 0, n-1
        while l<r:
            a = (r-l)*min(heights[l], heights[r])
            if a>max_a:
                max_a=a
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_a