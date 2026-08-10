class Solution:
    def trap(self, height: List[int]) -> int:
        
        #wo optim
        # ml, mr = [height[0]], [height[-1]]
        # for h in height[1:]:
        #     if h>ml[-1]:
        #         ml.append(h)
        #     else:
        #         ml.append(ml[-1])
        # for h in height[:-1][::-1]:
        #     if h>mr[-1]:
        #         mr.append(h)
        #     else:
        #         mr.append(mr[-1])
        # mr.reverse()
        # # print(ml, mr)
        # res = 0
        # for i, h in enumerate(height):
        #     r = min(ml[i], mr[i])-h
        #     res += r if r>0 else 0

        if not height: return 0
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0 
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res+=leftMax-height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res+=rightMax-height[r]            

        return res