class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = 0
        l, r = 0, len(heights)-1
        while l<r:
            min_ = min(heights[l],heights[r])
            maxa = max(maxa, (r-l)*min_)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return maxa 