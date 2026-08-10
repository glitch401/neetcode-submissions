class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            hm[n] = 1+hm.get(n,0)
        
        freqs = []
        for num,cnt in hm.items():
            freqs.append([cnt,num])
        freqs.sort()
        
        res = []
        while len(res)<k:
            res.append(freqs.pop()[1])

        return res

        