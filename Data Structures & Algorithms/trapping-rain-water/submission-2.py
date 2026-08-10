class Solution:
    def trap(self, height: List[int]) -> int:
        
        #wo optim
        ml, mr = [height[0]], [height[-1]]
        for h in height[1:]:
            if h>ml[-1]:
                ml.append(h)
            else:
                ml.append(ml[-1])
        for h in height[:-1][::-1]:
            if h>mr[-1]:
                mr.append(h)
            else:
                mr.append(mr[-1])
        mr.reverse()
        # print(ml, mr)
        res = 0
        for i, h in enumerate(height):
            r = min(ml[i], mr[i])-h
            res += r if r>0 else 0
        return res